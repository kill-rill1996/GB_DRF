import random
from datetime import datetime
from mixer.backend.django import mixer


from library.models import Book, Author


def random_year() -> int:
    """
    Pick random year from diapason
    :return: year (int)
    """
    return random.randint(1900, int(datetime.now().strftime("%Y")))


def add_authors(count) -> None:
    """
    Add count of authors in GET headers 'Number' to create them in DB
    :param count: count of authors to create
    :return: None
    """
    mixer.cycle(count).blend(Author, birthday_year=random_year)


def add_books(count) -> None:
    """
    Add count of authors in GET headers 'Number' to create them in DB
    :param count: count of authors to create
    :return: None
    """
    mixer.cycle(count).blend(Book, author=mixer.select)




