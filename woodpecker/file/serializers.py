from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):

    class Meta():
        model = File
        fields = ('id', 'file', 'remark', 'timestamp')


class FileListSerializer(serializers.ModelSerializer):

    file = serializers.CharField()
    remark = serializers.CharField(max_length=20)
    timestamp = serializers.DateTimeField()

    class Meta():
        model = File
        fields = ('id', 'file', 'remark', 'timestamp')
