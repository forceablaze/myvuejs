from django.shortcuts import render
from django.conf import settings
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

from .tasks import pecker_exec, add, search_text_task, search_log_exec

CVLOG_CACHE = {}
PER_PAGE_COUNT = 200

REVERSE_TABLE = {
 'funcid': None,
 'execreq': None,
}

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

class CVLogSearchView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    model = PeckerTask
    queryset = PeckerTask.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    serializer_class = PeckerTaskSerializer

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

    def searchLog(self, peckerTask, apitype, logFormat,
            text, hexs, params, formatted_texts, beforeAfter = 10):

        jsonFile = self.getLogJsonPath(peckerTask)

        r = search_log_exec.delay(peckerTask.log_id, jsonFile, apitype, logFormat, text,
            hexs, params, formatted_texts, beforeAfter)

        '''

        beforeAfterIndexs = []
        for idx in indexs:
            beforeAfterIndexs += [i for i in range(idx - 10, idx + 10)]

        return self.responseLogJSON(logObj, _logs, indexs)
        '''
        return Response({'task_id': r.id})

    def getLogJsonPath(self, peckerTask):

        fileStatus = None
        try:
            fileStatus = File.objects.get(id=peckerTask.log_id)
        except ObjectDoesNotExist:
            return None

        jsonFile = Path(Path(fileStatus.file.path).parent, peckerTask.output).resolve()

        return str(jsonFile)


    def showSearchResult(self, peckerTask):

        if not peckerTask.search:
            return Response({'message': 'Not search task.'})

        content = {}
        indexs = None
        try:
            f = open(Path(settings.MEDIA_ROOT, peckerTask.output), 'r')
            indexs = json.load(f)
            f.close()
        except ValueError:
            return Response({'message': 'JSON file format error'})
        except FileNotFoundError:
            return Response({'message': '{} not found.'.format(peckerTask.output)})

        parentPeckerTask = None
        try:
            parentPeckerTask = PeckerTask.objects.get(log_id=peckerTask.log_id, search=False)
        except ObjectDoesNotExist:
            return Response({'message': 'Invalid task.'})

        jsonFile = self.getLogJsonPath(parentPeckerTask)
        try:
            f = open(jsonFile, 'r')
            logObj = json.load(f)
            f.close()
        except ValueError:
            return Response({'error': 'JSON file format error.'}, status=status.HTTP_200_OK)
        except FileNotFoundError:
            return Response({'error': 'No file found.'}, status=status.HTTP_200_OK)

        _logs = logObj['logs']
        _logs = list(filter(lambda x:  x['index'] in indexs, _logs))

        return self.responseLogJSON(logObj, _logs, indexs)

    def post(self, request, task_id, *args, **kwargs):

        peckerTask = None
        try:
            peckerTask = PeckerTask.objects.get(task_id=task_id)
        except ObjectDoesNotExist:
            content = {'message': 'No such task_id id ({}) found.'.format(task_id)}
            return Response(content, status=status.HTTP_200_OK)

        # retrieve search result
        if 'retrieve' in request.data:
            if request.data['retrieve']:
                return self.showSearchResult(peckerTask)

        apitype = None
        log_format = None
        text = None
        hexs = None
        params = None
        formatted_texts = None

        if 'apitype' in request.data:
            apitype = request.data['apitype']
        if 'log_format' in request.data:
            log_format = request.data['log_format']
        if 'text' in request.data:
            text = request.data['text']
        if 'hexs' in request.data:
            hexs = request.data['hexs']
        if 'params' in request.data:
            params = request.data['params']

        if 'formatted_texts' in request.data:
            formatted_texts = request.data['formatted_texts']


        print('apitype: {}'.format(apitype))
        print('log_format: {}'.format(log_format))
        print('text: {}'.format(text))
        print('hexs: {}'.format(hexs))
        print('params: {}'.format(params))
        #params: {'funcid': {'name': 'FimsExecute', 'dest': 'logid'}, 'execreq': {'name': 'CursorClose', 'dest': 'part1'}}

        return self.searchLog(peckerTask, apitype, log_format,
                text, hexs, params, formatted_texts)
