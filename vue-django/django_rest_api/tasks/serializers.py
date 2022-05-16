
from rest_framework import routers, serializers, viewsets
from .models import Task
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'stage', 'created_at','timerState', 'timer']
        #fields = '__all__'
        
