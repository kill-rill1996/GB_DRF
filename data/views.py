import json

from django.shortcuts import redirect
from mixer.backend.django import mixer
from library.models import Book, Author

from .services.add_items import add_authors, add_books


def add_author_view(request):
    add_authors(int(request.headers['Number']))
    return redirect('/api/authors/')


def add_book_view(request):
    add_books(int(request.headers['Number']))
    return redirect('/api/books/')
