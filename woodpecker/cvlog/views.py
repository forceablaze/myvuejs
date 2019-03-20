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

        if int(log_id) == 999:
            count = 20000
            logTemplate = {   'index': 0, 'position': '0x0', 'seq': '213-213', 'time': '1003275879',
                        'flag': '0x250c4', 'dest': 'NVRAM', 'format': 'binary',
                        'direction': 'send', 'usage': '全体統合',
                        'logtype': 'Call 関数コール',
                        'loglevel': 'info', 'apitype': 'DbguServiceCall()',
                        'cputype': 0, 'logid': '0x060a',
                        'ownid': '', 'destid': '', 'taskid': '',
                        'formatted_result': 'abc',
                        'raw_payload': 'abc',
                        'payload_len': 16,
                        'binary_len': 16
                    }

            content = {
                'logtype': '40',
                'logs': []
            }

            for i in range(0, count):
                content['logs'].append(logTemplate)
            return Response(content)

        log = Log.objects.get(id=log_id)
        serializer = self.serializer_class(log)

        return Response(serializer.data, status=status.HTTP_200_OK)
