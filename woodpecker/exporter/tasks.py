from __future__ import absolute_import

import json, uuid, io, os
from django.core.exceptions import ObjectDoesNotExist
from celery import shared_task
from pathlib import Path
from django.conf import settings
# app instance
from woodpecker import celery_app
from woodpecker.utils import execute

from exporter.models import ExporterTask
from exporter.models import ExporterTaskStatus, ExporterTaskStatusToString
from file.models import File

@shared_task(bind=True)
def exporter_exec(self, log_id = None, uuid = None):
    if log_id is None:
        return
    if uuid is None:
        return
    fileStatus = None
    try:
        fileStatus = File.objects.get(id=log_id)
    except ObjectDoesNotExist:
        return
    
    targetPath = Path(Path(fileStatus.file.path).parent, uuid).resolve()
    print('{} export target'.format(targetPath))
    
    # task id
    taskUUIDStr = exporter_exec.request.id
    exporterTask = ExporterTask(task_id = taskUUIDStr,
        status = ExporterTaskStatusToString(ExporterTaskStatus.CREATED),
        log_id = log_id,
        output = uuid)
    exporterTask.save()
    
    exporterTask.status = ExporterTaskStatusToString(ExporterTaskStatus.RUNNING)
    exporterTask.save()
    
    logObj = None
    try:
        f = open(targetPath, 'r')
        logObj = json.load(f)
        f.close()
    except ValueError:
        print('JSON file format error')
        exporterTask.status = ExporterTaskStatusToString(ExporterTaskStatus.FAILED)
    except FileNotFoundError:
        print('{} not found.'.format(outputFilePath))
        exporterTask.status = ExporterTaskStatusToString(ExporterTaskStatus.FAILED)
    
    txtbuff = io.StringIO()
    logsValues = logObj['logs']
    
    for value in logsValues:
        txtbuff.write('{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}\n'.format(
            value.get('index')         , value.get('time')       , value.get('apitype')   ,
            value.get('direction')     , value.get('own_domain') , value.get('own_subsys'),
            value.get('dest_domain')   , value.get('dest_subsys'), value.get('own_domain'),
            value.get('formatted_text'), value.get('binary_text')
            ))

    textFilePath = Path(settings.MEDIA_ROOT, exporterTask.output + '.txt').resolve()
    try:
        f = open(textFilePath, 'w')
        f.write(txtbuff.getvalue())
        f.close()
    except ValueError:
        print('file format error')
        exporterTask.status = ExporterTaskStatusToString(ExporterTaskStatus.FAILED)
    except FileNotFoundError:
        print('{} not found.'.format(textFilePath))
        exporterTask.status = ExporterTaskStatusToString(ExporterTaskStatus.FAILED)

    txtbuff.close()
  
    exporterTask.status = ExporterTaskStatusToString(ExporterTaskStatus.SUCCESS)
    exporterTask.save()
