from rest_framework import serializers

from .models import ExporterStatus
from .models import ExporterTask


class ExporterTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExporterTask
        exclude = ('id',)