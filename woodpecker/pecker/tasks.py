from __future__ import absolute_import

import json, uuid
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

def createCVLog(fileStatus, obj):
    return CVLog(
        file = fileStatus, 
        product = obj['product'],
        serial_number = obj['serial_number'],
        time = obj['time'],
        LG = obj['LG'],
        logtype = obj['logtype'],
        addr_code = obj['addr_code']
    )

def importLogMeta(cvlog, logsObj):

    for log in logsObj:
        logMeta = LogMeta(
            cvlog = cvlog,
            index = log['index'],
            position = log['position'],
            seq = log['seq'],
            time = log['time'],
            flag = log['flag'],
            dest = log['dest'],
            format = log['format'],
            direction = log['direction'],
            usage = log['usage'],
            logtype = log['logtype'],
            loglevel = log['loglevel'],
            apitype = log['apitype'],
            logid = log['logid'],
            own_domain = log['own_domain'],
            own_subsys = log['own_subsys'],
            dest_domain = log['dest_domain'],
            dest_subsys = log['dest_subsys'],
            task_domain = log['task_domain'],
            task_subsys = log['task_subsys']
        )
        logMeta.save()

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

