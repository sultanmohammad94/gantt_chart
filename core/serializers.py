from dataclasses import field
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Task, Link


class TaskSerializer(ModelSerializer):
    """This class is responsible for serializing DXHTML Task."""
    
    start_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    end_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    
    class Meta:
        model = Task
        fields = (
            'id', 'text', 'start_date','end_date',
            'duration', 'progress','parent'
            )
        


class LinkSerializer(ModelSerializer):
    """This class is responsible for serializing DXHTML Link."""
    class Meta:
        model = Link
        fields = (
            'id', 'source', 'target',
            'type', 'lag'
        )