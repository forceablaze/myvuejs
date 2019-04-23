from __future__ import absolute_import

import json, uuid, io
from django.core.exceptions import ObjectDoesNotExist
from celery import shared_task
from pathlib import Path

# app instance
from woodpecker import celery_app

from woodpecker.settings import CVLOG_UTIL_PATH
from woodpecker.utils import execute

from file.models import File
from pecker.models import PeckerTask
from pecker.models import PeckerTaskStatus, PeckerTaskStatusToString

from pecker.models import CVLog, LogMeta

import re

@shared_task
def add(x, y):
    return x + y

@shared_task(bind=True)
def search_text_task(self, string, seq, pattern):
    indexs = []

    for m in re.finditer(string, seq):

        # find the magic number
        res = re.finditer(pattern[::-1], seq[m.start() - 1::-1])
        it = iter(res)
        a = next(it)

        # find the index of log
        subseq = seq[0:m.start()]
        res = re.match('\d+FF', subseq[len(subseq) - a.start():])
        if res:
            index = int(res.group(0)[:len(res.group(0)) - 2])
            indexs.append(index)

    return indexs

def searchText(logs, string):
    print('searchText')

    MAGIC_NUMBER = bytearray.fromhex('494e544547')
    pattern = MAGIC_NUMBER.decode()

    strIO = io.StringIO()

    for i in range(0, len(logs)):
        log = logs[i]
        if 'text' not in log:
            continue
        text = log['text']

        strIO.write(pattern)
        strIO.write(str(log['index']) + 'FF')
        strIO.write(text)

    seq = strIO.getvalue()
    strIO.close()
    indexs = search_text_task(string, seq, pattern)

    return list(filter(lambda x:  x['index'] in indexs, logs))

def searchHexString(logs, hexString):
    print('searchHexString')

    MAGIC_NUMBER = bytearray.fromhex('494e544547')
    pattern = MAGIC_NUMBER.decode()

    strIO = io.StringIO()

    for i in range(0, len(logs)):
        log = logs[i]

        text = ''
        for record in log['raw']:
            for part in record:
                text += part

        strIO.write(pattern)
        strIO.write(str(log['index']) + 'FF')
        strIO.write(text)

    seq = strIO.getvalue()
    strIO.close()
    indexs = search_text_task(hexString.lower(), seq, pattern)

    return list(filter(lambda x:  x['index'] in indexs, logs))

@shared_task(bind=True)
def search_log_exec(self, peckerTask, apitype, log_format, text,
        hexString, params_items, beforeAfter):

    fileStatus = None
    try:
        fileStatus = File.objects.get(id=peckerTask.log_id)
    except ObjectDoesNotExist:
        content = {'message': 'No such log id ({}) found.'.format(peckerTask.log_id)}
        return Response(content, status=status.HTTP_200_OK)

    jsonFile = Path(Path(fileStatus.file.path).parent, peckerTask.output).resolve()
    print('read {}'.format(jsonFile))

    content = {'error': 'something error.'}

    try:
        f = open(jsonFile, 'r')
        logObj = json.load(f)
    except ValueError:
        print('JSON file format error')
        return Response({'error': 'JSON file format error.'}, status=status.HTTP_200_OK)
    except FileNotFoundError:
        print('{} not found.'.format(jsonFile))
        return Response({'error': 'No file found.'}, status=status.HTTP_200_OK)
     #originLogs = copy.deepcopy(logObj['logs'])
    _logs = logObj['logs']
    if apitype:
        _logs = list(filter(lambda x: x['apitype'] == apitype, _logs))
    if log_format:
        _logs = list(filter(lambda x: x['format'] == log_format, _logs))
    if text:
        _logs = searchText(_logs, text)
    elif hexString:
        print('search hex')
        _logs = searchHexString(_logs, hexString)

    return [logObj, _logs]

@shared_task(bind=True)
def pecker_exec(self, log_id = None):

    if log_id is None:
        return

    fileStatus = None
    try:
        fileStatus = File.objects.get(id=log_id)
    except ObjectDoesNotExist:
        return


    binaryPath = Path(CVLOG_UTIL_PATH)
    outputUUID = str(uuid.uuid4())
    outputFilePath = Path(Path(fileStatus.file.path).parent, outputUUID).resolve()

    cvlog_args = [
        '-a',
        '--json', outputFilePath,
        '-b', fileStatus.file.path,
        '-t', Path(Path(binaryPath).parent, 'debug-symbol/logFormatSymbolsCv2kCS.csv').resolve()
    ]

    print(outputFilePath)

    # task id
    taskUUIDStr = pecker_exec.request.id

    peckerTask = PeckerTask(task_id = taskUUIDStr,
        status = PeckerTaskStatusToString(PeckerTaskStatus.CREATED),
        log_id = log_id,
        output = outputUUID)
    peckerTask.save()


    peckerTask.status = PeckerTaskStatusToString(PeckerTaskStatus.RUNNING)
    peckerTask.save()

    # execute cvlog
    result = execute(CVLOG_UTIL_PATH, cvlog_args, cwd = binaryPath.parent)

    logObj = None
    peckerTask.status = PeckerTaskStatusToString(PeckerTaskStatus.SUCCESS)
    try:
        f = open(outputFilePath, 'r')
        logObj = json.load(f)
        f.close()
    except ValueError:
        print('JSON file format error')
        peckerTask.status = PeckerTaskStatusToString(PeckerTaskStatus.FAILED)
    except FileNotFoundError:
        print('{} not found.'.format(outputFilePath))
        peckerTask.status = PeckerTaskStatusToString(PeckerTaskStatus.FAILED)

    #cvlog = createCVLog(fileStatus, logObj)
    #cvlog.save()

    #importLogMeta(cvlog, logObj['logs'])

    peckerTask.save()

