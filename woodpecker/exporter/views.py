from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from django.http import StreamingHttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from wsgiref.util import FileWrapper

from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework import status
from .models import ExporterTask
from .serializers import ExporterTaskSerializer

from pathlib import Path
import json, uuid, io, os

from .tasks import exporter_exec
from file.models import File

# Create your views here.
class ExpoterTaskStatusView(RetrieveAPIView):

    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    serializer_class = ExporterTaskSerializer

    def retrieve(self, request, task_id, *args, **kwargs):
        exporterTask = None
        try:
            exporterTask = ExporterTask.objects.get(task_id=task_id)
        except ObjectDoesNotExist:
            print('No such exporter task id ({}) found.'.format(task_id))
            return HttpResponseNotFound('{} exporter task not found.'.format(task_id))

        serializer = self.serializer_class(exporterTask)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ExpoterTaskCreateView(GenericAPIView):
    model = ExporterTask
    permission_classes = (AllowAny, )
    renderer_classes = (JSONRenderer, )
    
    def post(self, request, *args, **kwargs):
        try:
            log_id = request.data['log_id']
            uuid   = request.data['uuid']
        except Exception as e:
            print(e)
            return HttpResponse(status = status.HTTP_406_NOT_ACCEPTABLE)

        r = exporter_exec.delay(log_id, uuid)

        return Response({'task_id': r.id})

class ExpoterFileView(GenericAPIView):
    permission_classes = (AllowAny, )

    def get(self, request, uuid, *args, **kwargs):

        chunk_size = 8192
        downloadPath = Path(settings.MEDIA_ROOT, str(uuid)).resolve()

        response = StreamingHttpResponse(
            FileWrapper(open(downloadPath, 'rb'), chunk_size),
            content_type="text/plain")


        exporterTask = ExporterTask.objects.get(output = str(uuid))

        fileStatus = None
        try:
            fileStatus = File.objects.get(id=exporterTask.log_id)
        except ObjectDoesNotExist:
            return
        logName = Path(fileStatus.file.path).name

        print('get the export result of {}'.format(logName))

        response['Content-Length'] = os.path.getsize(downloadPath)
        response['Content-Disposition'] = "attachment; filename={}".format(logName + '.txt')

        return response
