from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorModelSerializer


class AuthorModelViewSets(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
