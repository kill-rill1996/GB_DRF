from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Project, ToDo
from .serializers import ProjectsModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsModelSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer

