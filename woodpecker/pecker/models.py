from django.db import models
from enum import Enum

from file.models import File

class PeckerTaskStatus(Enum):
    CREATED = 1
    RUNNING = 2
    INTERRUPTED = 3
    STOPPED = 4
    SUCCESS = 5
    FAILED = 6

PeckerTaskStatusMap = {
    PeckerTaskStatus.CREATED: 'created',
    PeckerTaskStatus.RUNNING: 'running',
    PeckerTaskStatus.INTERRUPTED: 'interrupted',
    PeckerTaskStatus.SUCCESS: 'success',
    PeckerTaskStatus.FAILED: 'failed',
    PeckerTaskStatus.STOPPED: 'stopped',
}


def PeckerTaskStatusToString(status):
    return PeckerTaskStatusMap[status]

# Create your models here.
class PeckerStatus(models.Model):

    logid = models.IntegerField()

    status = models.CharField(max_length=20)


class PeckerTask(models.Model):

    task_id = models.CharField(max_length=32, blank=True, unique=True)

    status = models.CharField(max_length=20)

    log_id = models.IntegerField()

    output = models.CharField(max_length=80)

    timestamp = models.DateTimeField(auto_now_add=True)

class CVLog(models.Model):

    file = models.ForeignKey(File, on_delete=models.CASCADE)

    product = models.CharField(max_length=32)
    serial_number = models.CharField(max_length=32)

    time = models.CharField(max_length=20)
    LG = models.CharField(max_length=20)
    logtype = models.CharField(max_length=4)
    addr_code = models.CharField(max_length=8)

class LogMeta(models.Model):

    cvlog = models.ForeignKey(CVLog, on_delete=models.CASCADE)

    index = models.IntegerField()
    position = models.CharField(max_length=80)

    seq = models.CharField(max_length=10)
    time = models.CharField(max_length=80)
    flag = models.CharField(max_length=8)
    dest = models.CharField(max_length=80)

    format = models.CharField(max_length=10)
    direction = models.CharField(max_length=10)
    usage = models.CharField(max_length=80)
    logtype = models.CharField(max_length=80)
    loglevel = models.CharField(max_length=80)
    apitype = models.CharField(max_length=80)

    logid = models.CharField(max_length=8)

    own_domain = models.CharField(max_length=80)
    own_subsys = models.CharField(max_length=80)

    dest_domain = models.CharField(max_length=80)
    dest_subsys = models.CharField(max_length=80)

    task_domain = models.CharField(max_length=80)
    task_subsys = models.CharField(max_length=80)

    class Meta:
        ordering = ('cvlog', 'index',)
