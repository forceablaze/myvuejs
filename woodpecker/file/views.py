from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import FileSerializer, FileListSerializer
from .models import File

from rest_framework.renderers import JSONRenderer

class FileView(APIView):

    parser_classes = (MultiPartParser, FormParser)
    renderer_classes = (JSONRenderer, )

    def get(self, request, format = None):
        logs = File.objects.all()
        serializer = FileSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
