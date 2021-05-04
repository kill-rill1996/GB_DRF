from rest_framework.pagination import PageNumberPagination


class ProjectPageNumberPagination(PageNumberPagination):
    page_size = 1


class TodoPagination(PageNumberPagination):
    page_size = 20