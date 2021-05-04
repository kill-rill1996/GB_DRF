import mixins as mixins
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin


import logging

from .models import User
from .serializers import UserModelSerializer


logger = logging.getLogger('service_log')


class UserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    logger.info(f'Log from {__name__} app users')
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
