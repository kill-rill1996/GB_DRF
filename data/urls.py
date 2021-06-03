from django.contrib import admin
from django.urls import path, include

from .views import add_author_view, add_book_view

urlpatterns = [
    path('authors/', add_author_view),
    path('books/', add_book_view),

]
