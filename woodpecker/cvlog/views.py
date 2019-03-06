from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.generics import GenericAPIView

from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework import mixins

from .models import Log
from .renderers import LogJSONRenderer
from .serializers import LogListSerializer, LogSerializer

# Create your views here.

class LogListAPIView(ListAPIView):
    model = Log
    queryset = Log.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (LogJSONRenderer, )
    serializer_class = LogListSerializer

class LogListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    model = Log
    queryset = Log.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (LogJSONRenderer, )
    serializer_class = LogListSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        content = {'test': 'hello'}
        return Response(content)

class LogRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (LogJSONRenderer, )
    serializer_class = LogSerializer

    def retrieve(self, request, log_id, *args, **kwargs):
        log = Log.objects.get(id=log_id)
        serializer = self.serializer_class(log)

        return Response(serializer.data, status=status.HTTP_200_OK)
