import random
from datetime import datetime
from mixer.backend.django import mixer

from library.models import Book, Author

URLS = {
    'books': Book,
    'authors': Author,
}


def parse_path(request: object) -> str:
    """Parse url and take last domen"""
    return request.path.replace("/", ' ').split()[-1]


def get_number_of_items(request: object) -> int:
    """Get number of models to create"""
    try:
        return int(request.headers['Number'])
    except KeyError:
        return 1


def get_key_from_value(dict, value):
    for key, v in dict.items():
        if v == value:
            return key


def add_items(request: object) -> str:
    """Create objects in DB and return str model for redirect url"""

    model = URLS[parse_path(request)]
    count = get_number_of_items(request)
    if model == Book:
        if Author.objects.all():
            mixer.cycle(count).blend(model, author=mixer.select)
        else:
            mixer.cycle(count).blend(model)
    else:
        mixer.cycle(count).blend(model)
    return get_key_from_value(URLS, model)
