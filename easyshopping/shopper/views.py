from django.shortcuts import render
from .models import Good, Shop


def index(request):

    shops = Shop.objects.all()

    return render(request, 'shopper/index.html', {
        'shops': shops,
    })