from django.shortcuts import render
import logging
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorModelSerializer

logger = logging.getLogger('service_log')


class AuthorModelViewSets(ModelViewSet):
    logger.info('Сработала вьюха авторов')
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
