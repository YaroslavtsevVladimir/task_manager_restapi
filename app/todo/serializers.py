from rest_framework_json_api import serializers
from .models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
            'created',
            'changed',
            'deadline',
            'priority',
            'completed',
            'completed_date'
        )
