from django.shortcuts import redirect
from .services.add_items import add_items


def add_items_view(request):
    model_url = add_items(request)
    return redirect(f'/api/{model_url}')

