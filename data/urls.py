from django.contrib import admin
from django.urls import path, include

from .views import add_items_view

urlpatterns = [
    path('authors/', add_items_view),
    path('books/', add_items_view),

]
