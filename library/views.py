from django.shortcuts import render
import logging

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book
from .serializers import AuthorModelSerializer, BookModelSerializer

logger = logging.getLogger('service_log')


class AuthorModelViewSet(ModelViewSet):
    logger.info('Сработала вьюха авторов')
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


