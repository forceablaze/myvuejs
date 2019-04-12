from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.generics import GenericAPIView, ListAPIView

from rest_framework.renderers import JSONRenderer

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import PeckerTask
from .serializers import PeckerTaskSerializer

from rest_framework import mixins

import io, re
import json
import copy
from pathlib import Path
from file.models import File

from .tasks import pecker_exec, add, search_text_task

CVLOG_CACHE = {}
PER_PAGE_COUNT = 200

# Create your views here.
class PeckerTaskStatusView(RetrieveAPIView):

    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    serializer_class = PeckerTaskSerializer

    def retrieve(self, request, task_id, *args, **kwargs):

        peckerTask = None
        try:
            peckerTask = PeckerTask.objects.get(task_id=task_id)
        except ObjectDoesNotExist:
            content = {'message': 'No such pecker task id ({}) found.'.format(task_id)}
            return Response(content, status=status.HTTP_200_OK)

        serializer = self.serializer_class(peckerTask)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PeckerTaskCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    model = PeckerTask
    queryset = PeckerTask.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    serializer_class = PeckerTaskSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        try:
            log_id = request.data['log_id']
        except Exception as e:
            print(e)
            content = {'error': 'invalid data'}
            return Response(content)

        r = pecker_exec.delay(log_id)

        return Response({'task_id': r.id})

class CVLogRetrieveView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def responseLogJSON(self, peckerTask, log_from = 0, log_to = None, count = PER_PAGE_COUNT):
        print('fetch log json log_id: {}, from: {}, to: {}, count: {}'.format(
            peckerTask.log_id, log_from, log_to, count))

        fileStatus = None
        try:
            fileStatus = File.objects.get(id=peckerTask.log_id)
        except ObjectDoesNotExist:
            content = {'message': 'No such log id ({}) found.'.format(peckerTask.log_id)}
            return Response(content, status=status.HTTP_200_OK)

        jsonFile = Path(Path(fileStatus.file.path).parent, peckerTask.output).resolve()
        print('read {}'.format(jsonFile))

        content = {'error': 'something error.'}

        if peckerTask.task_id not in CVLOG_CACHE:
            print('NO CACHE FOUND')
            try:
                f = open(jsonFile, 'r')
                logObj = json.load(f)
                CVLOG_CACHE[peckerTask.task_id] = logObj
            except ValueError:
                print('JSON file format error')
                return Response({'error': 'JSON file format error.'}, status=status.HTTP_200_OK)
            except FileNotFoundError:
                print('{} not found.'.format(jsonFile))
                return Response({'error': 'No file found.'}, status=status.HTTP_200_OK)

        print('{} {}'.format(log_from, log_from + count))
        content = {}
        content['product'] = CVLOG_CACHE[peckerTask.task_id]['product']
        content['serial_number'] = CVLOG_CACHE[peckerTask.task_id]['serial_number']
        content['time'] = CVLOG_CACHE[peckerTask.task_id]['time']
        content['LG'] = CVLOG_CACHE[peckerTask.task_id]['LG']
        content['logtype'] = CVLOG_CACHE[peckerTask.task_id]['logtype']
        content['addr_code'] = CVLOG_CACHE[peckerTask.task_id]['addr_code']
        content['logs'] = CVLOG_CACHE[peckerTask.task_id]['logs'][log_from: log_from + count]
        content['log_total_number'] = len(CVLOG_CACHE[peckerTask.task_id]['logs'])
        if content['log_total_number'] % count != 0:
            content['total_pages'] = int(content['log_total_number'] / count) + 1
        else:
            content['total_pages'] = int(content['log_total_number'] / count) + 1

        return Response(content, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # get task by log_id
        try:
            task_id = request.data['task_id']
        except Exception as e:
            print(e)
            content = {'error': 'invalid data'}
            return Response(content)

        log_from = 0
        count = PER_PAGE_COUNT
        log_to = None
        if 'from' in request.data:
            log_from = request.data['from']
        if 'count' in request.data:
            count = request.data['count']
        if 'to' in request.data:
            log_to = request.data['to']

        try:
            peckerTask = PeckerTask.objects.get(task_id=task_id)
        except ObjectDoesNotExist:
            content = {'message': 'No such task_id id ({}) found.'.format(task_id)}
            return Response(content, status=status.HTTP_200_OK)

        return self.responseLogJSON(peckerTask, log_from, log_to, count)

    def retrieve(self, request, task_id, *args, **kwargs):

        peckerTask = None
        try:
            peckerTask = PeckerTask.objects.get(task_id=task_id)
        except ObjectDoesNotExist:
            content = {'message': 'No such task_id id ({}) found.'.format(task_id)}
            return Response(content, status=status.HTTP_200_OK)

        return self.responseLogJSON(peckerTask)

class CVLogSearchView(mixins.CreateModelMixin, GenericAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def responseLogJSON(self, logObj, logs, indexs):

        content = {}
        content['product'] = logObj['product']
        content['serial_number'] = logObj['serial_number']
        content['time'] = logObj['time']
        content['LG'] = logObj['LG']
        content['logtype'] = logObj['logtype']
        content['addr_code'] = logObj['addr_code']
        content['logs'] = logs
        content['log_total_number'] = len(logs)
        content['indexs'] = indexs
        if content['log_total_number'] % PER_PAGE_COUNT != 0:
            content['total_pages'] = int(content['log_total_number'] / PER_PAGE_COUNT) + 1
        else:
            content['total_pages'] = int(content['log_total_number'] / PER_PAGE_COUNT) + 1

        return Response(content, status=status.HTTP_200_OK)

    def searchLog(self, peckerTask, apitype, log_format, text, hexString, beforeAfter = 10):

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
            _logs = self.searchText(_logs, text)
        elif hexString:
            print('search hex')
            _logs = self.searchHexString(_logs, hexString)

        indexs = [ log['index'] for log in _logs ]
        '''

        beforeAfterIndexs = []
        for idx in indexs:
            beforeAfterIndexs += [i for i in range(idx - 10, idx + 10)]
 
        _logs = list(filter(lambda x:  x['index'] in beforeAfterIndexs, originLogs))
        '''

        return self.responseLogJSON(logObj, _logs, indexs)

    def searchText(self, logs, string):
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

    def searchHexString(self, logs, hexString):
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


    def post(self, request, task_id, *args, **kwargs):
        # get task by log_id

        peckerTask = None
        try:
            peckerTask = PeckerTask.objects.get(task_id=task_id)
        except ObjectDoesNotExist:
            content = {'message': 'No such task_id id ({}) found.'.format(task_id)}
            return Response(content, status=status.HTTP_200_OK)

        apitype = None
        logFormat = None
        text = None
        hexs = None

        if 'apitype' in request.data:
            apitype = request.data['apitype']
        if 'logFormat' in request.data:
            logFormat = request.data['log_format']
        if 'text' in request.data:
            text = request.data['text']
        if 'hexs' in request.data:
            hexs = request.data['hexs']

        print('apitype: {}'.format(apitype))
        print('log_format: {}'.format(logFormat))
        print('text: {}'.format(text))
        print('hexs: {}'.format(hexs))

        return self.searchLog(peckerTask, apitype, logFormat, text, hexs)
