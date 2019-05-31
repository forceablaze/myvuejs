from django.db import models
from enum import Enum

class ExporterTaskStatus(Enum):
    CREATED = 1
    RUNNING = 2
    INTERRUPTED = 3
    STOPPED = 4
    SUCCESS = 5
    FAILED = 6

ExporterTaskStatusMap = {
    ExporterTaskStatus.CREATED: 'created',
    ExporterTaskStatus.RUNNING: 'running',
    ExporterTaskStatus.INTERRUPTED: 'interrupted',
    ExporterTaskStatus.SUCCESS: 'success',
    ExporterTaskStatus.FAILED: 'failed',
    ExporterTaskStatus.STOPPED: 'stopped',
}


def ExporterTaskStatusToString(status):
    return ExporterTaskStatusMap[status]

# Create your models here.
class ExporterStatus(models.Model):

    logid = models.IntegerField()

    status = models.CharField(max_length=20)


class ExporterTask(models.Model):

    task_id = models.CharField(max_length=32, blank=True, unique=True)

    status = models.CharField(max_length=20)

    log_id = models.IntegerField()

    output = models.CharField(max_length=80)

    timestamp = models.DateTimeField(auto_now_add=True)