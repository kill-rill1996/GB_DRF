from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField

from .models import Project, ToDo
from users.models import User


class UserProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    users = UserProjectSerializer(many=True)

    class Meta:
        model = Project
        fields = ['uuid', 'title', 'users', 'git_repository']


class ToDoModelSerializer(HyperlinkedModelSerializer):
    user = UserProjectSerializer()
    project = ProjectsModelSerializer()

    class Meta:
        model = ToDo
        fields = ['uuid', 'user', 'project', 'text', 'time_created', 'time_changed', 'is_active']