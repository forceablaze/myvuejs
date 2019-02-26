from rest_framework import serializers
from .models import Log

class LogListSerializer(serializers.ModelSerializer):

    logtype = serializers.CharField(max_length = 2)

    logsize = serializers.IntegerField()

    uploaded_at = serializers.DateTimeField()

    class Meta:
        model = Log
        field = ('id', 'logtype', 'logsize', 'uploaded_at')

class LogSerializer(serializers.ModelSerializer):

    logtype = serializers.CharField(max_length = 2)

    logsize = serializers.IntegerField()

    uploaded_at = serializers.DateTimeField()

    class Meta:
        model = Log
        field = ('id', 'logtype', 'logsize', 'uploaded_at')
