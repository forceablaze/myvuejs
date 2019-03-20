from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from woodpecker.messages import NoFileIdFoundMessage

# Create your views here.
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import FileSerializer
from .models import File

from rest_framework.renderers import JSONRenderer

class FileStatusView(RetrieveAPIView):

    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    serializer_class = FileSerializer

    def retrieve(self, request, id, *args, **kwargs):

        fileStatus = None
        try:
            fileStatus = File.objects.get(id=id)
        except ObjectDoesNotExist:
            content = NoFileIdFoundMessage.getMessage(id)
            return Response(content, status=status.HTTP_200_OK)

        serializer = self.serializer_class(fileStatus)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
