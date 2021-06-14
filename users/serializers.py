from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserModelSerializer2(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'is_staff', 'is_superuser']
