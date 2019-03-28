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

import json
from pathlib import Path
from file.models import File

from .tasks import pecker_exec, add

CVLOG_CACHE = {}

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

    def responseLogJSON(self, peckerTask, log_from = 0, log_to = None, count = 50):
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

        content = CVLOG_CACHE[peckerTask.task_id]
        content['logs'] = CVLOG_CACHE[peckerTask.task_id]['logs'][log_from: log_from + count]

        return Response(content, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        # get task by log_id
        try:
            log_id = request.data['log_id']
        except Exception as e:
            print(e)
            content = {'error': 'invalid data'}
            return Response(content)

        log_from = 0
        count = 50
        log_to = None
        if 'from' in request.data:
            log_from = request.data['from']
        if 'count' in request.data:
            count = request.data['count']
        if 'to' in request.data:
            log_to = request.data['to']

        try:
            peckerTask = PeckerTask.objects.get(log_id=log_id)
        except MultipleObjectsReturned as e:
            peckerTask = PeckerTask.objects.filter(
                log_id=log_id).order_by('timestamp')[0]
        except ObjectDoesNotExist:
            content = {'message': 'No such task with log id ({}) found.'.format(log_id)}
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
