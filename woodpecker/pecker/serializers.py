from rest_framework import serializers

from .models import PeckerStatus
from .models import PeckerTask

from .models import CVLog, LogMeta

class PeckerTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeckerTask
        exclude = ('id',)

class CVLogObjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = CVLog

class LogMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogMeta
