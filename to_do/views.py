from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import logging
from .models import Project, ToDo
from .serializers import ProjectsModelSerializer, ToDoModelSerializer
from .pagination import ProjectPageNumberPagination, TodoPagination
from .filters import TodoFilter

logger = logging.getLogger('service_log')


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    logger.info(f'Сработала вьюха {__name__}')
    serializer_class = ProjectsModelSerializer
    # pagination_class = ProjectPageNumberPagination

    # Фильтрация через get_queryset
    def get_queryset(self):
        projects = Project.objects.all()
        title = self.request.query_params.get('title', '')
        if title:
            projects = Project.objects.filter(title__icontains=title)
        return projects


# Filter with django-filters
class TodoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    filterset_class = TodoFilter
    # filterset_fields = ['text', 'project']
    # pagination_class = TodoPagination

    def destroy(self, request, *args, **kwargs):
        to_do = get_object_or_404(ToDo, pk=kwargs['pk'])
        to_do.is_active = False
        to_do.save()
        logger.info(f'Заметка {to_do} была выполнена')
        return Response(status=201)







