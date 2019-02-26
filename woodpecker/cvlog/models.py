from django.db import models

# Create your models here.

types = {
    "10": "NORMAL",
    "20": "BUG",
    "30": "ERRRO",
    "40": "CP_DETAIL",
    "41": "NET_DETAIL",
    "4A": "CP_DETAIL_WATCHDOG",
    "4B": "NET_DETAIL_WATCHDOG",
    "50": "SYSTEM"
}

class Log(models.Model):

    logtype = models.CharField(max_length = 2)

    logsize = models.IntegerField()

    uploaded_at = models.DateTimeField()

    class Meta:
        ordering = ('uploaded_at',)
