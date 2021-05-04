from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField

from .models import Project, ToDo
from users.models import User


class UserProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ToDoModelSerializer(HyperlinkedModelSerializer):
    user = UserProjectSerializer()
    project = StringRelatedField()

    class Meta:
        model = ToDo
        fields = ['user', 'project', 'text', 'time_created', 'time_changed', 'is_active']


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    users = UserProjectSerializer(many=True)
    to_do = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['title', 'users', 'git_repository', 'to_do']
