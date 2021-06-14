import mixins as mixins
from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin


import logging

from .models import User
from .serializers import UserModelSerializer, UserModelSerializer2


logger = logging.getLogger('service_log')


class UserListAPIView(generics.ListAPIView):
    logger.info(f'Log from {__name__} app users')
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1.0':
            return UserModelSerializer
        elif self.request.version == '2.0':
            return UserModelSerializer2
