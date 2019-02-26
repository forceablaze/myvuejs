from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

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

class LogRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny, )
    renderer_classes = (LogJSONRenderer, )
    serializer_class = LogSerializer

    def retrieve(self, request, log_id, *args, **kwargs):
        log = Log.objects.get(id=log_id)
        serializer = self.serializer_class(log)

        return Response(serializer.data, status=status.HTTP_200_OK)
