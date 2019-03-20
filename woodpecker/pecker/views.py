from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

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
        return self.create(request, *args, **kwargs)

        content = {'test': 'hello'}
        return Response(content)

class CVLogRetrieveView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )

    def retrieve(self, request, task_id, *args, **kwargs):

        peckerTask = None
        try:
            peckerTask = PeckerTask.objects.get(task_id=task_id)
        except ObjectDoesNotExist:
            content = {'message': 'No such task_id id ({}) found.'.format(task_id)}
            return Response(content, status=status.HTTP_200_OK)

        fileStatus = None
        try:
            fileStatus = File.objects.get(id=peckerTask.log_id)
        except ObjectDoesNotExist:
            content = {'message': 'No such log id ({}) found.'.format(peckerTask.log_id)}
            return Response(content, status=status.HTTP_200_OK)

        jsonFile = Path(Path(fileStatus.file.path).parent, peckerTask.output).resolve()
        content = {'test': 'hello'}
        try:
            f = open(jsonFile, 'r')
            logObj = json.load(f)
            content = logObj
        except ValueError:
            print('JSON file format error')
            content = {'test': 'hello'}
        except FileNotFoundError:
            print('{} not found.'.format(jsonFile))

        return Response(content, status=status.HTTP_200_OK)
