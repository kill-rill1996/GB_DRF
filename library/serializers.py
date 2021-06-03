from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import Author, Book


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookModelSerializer(ModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Book
        fields = '__all__'

