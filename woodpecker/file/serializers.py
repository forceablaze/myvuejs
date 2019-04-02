from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):

    file_size = serializers.SerializerMethodField()

    class Meta():
        model = File
        fields = ('id', 'file', 'remark', 'file_size', 'timestamp')
        depath = 1

    def get_file_size(self, file):
        file_size = file.file.size
        return file_size
