from django_filters import rest_framework as filters
from .models import ToDo


class TodoFilter(filters.FilterSet):
    text = filters.CharFilter(lookup_expr='contains', field_name='text')
    project__title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ToDo
        fields = ['text', 'project']
