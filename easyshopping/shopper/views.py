import json

import simplejson as simplejson
from django.contrib.auth import logout
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .models import ProductsDescription, Products


class IndexView(TemplateView):
    template_name = 'shopper/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_hit'] = Products.objects.select_related().values(
            'productsdescription__product_name',
            'productsdescription__product_images',
        ).filter(productsdescription__product_is_hit=True)

        context['is_sale'] = Products.objects.select_related().values(
            'productsdescription__product_name',
            'productsdescription__product_images',
        ).filter(productsdescription__product_is_on_sale=True)

        return context

def sales_hits(request):
    """ API responsible for section of sales hits """

    start = int(request.GET.get('start') or 0)
    end = int(request.GET.get('end') or start)

    query = Products.objects.select_related().values(
            'productsdescription__product_name',
            'productsdescription__product_images',
        ).filter(productsdescription__product_is_hit=True).distinct()

    json_objects = simplejson.dumps([item for item in query])

    json_data = json.loads(json_objects)

    # Create list and fill it by objects
    data = []
    try:
        for i in range(start, end):
            data.append(json_data[i])
    except IndexError:
        pass

    return JsonResponse(
        {
            'products': data,
            'length': len(json_data),
         },
    )
