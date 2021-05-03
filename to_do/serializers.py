from rest_framework.serializers import ModelSerializer, \
    HyperlinkedModelSerializer, \
    StringRelatedField

from .models import Project, ToDo
from users.serializers import UserModelSerializer


class ToDoModelSerializer(ModelSerializer):
    user = UserModelSerializer()
    project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = ['user', 'project', 'text', 'time_created', 'time_changed']


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer(many=True)
    to_do = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['title', 'users', 'git_repository', 'to_do']