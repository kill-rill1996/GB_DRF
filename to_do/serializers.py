from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Project, ToDo
from users.serializers import UserModelSerializer


class ToDoModelSerializer(HyperlinkedModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = ToDo
        fields = ['user', 'project', 'text', 'time_created', 'time_changed']


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = ['title', 'users', 'git_repository']