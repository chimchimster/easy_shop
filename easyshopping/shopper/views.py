import json

import simplejson
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

        return context


def response_api(func):
    """ Renders JsonResponse objects. """

    def wraps(*args, **kwargs):

        # Retrieving request from args
        request = args[0]

        # Applying initial settings for lazy load
        start = int(request.GET.get('start') or 0)
        end = int(request.GET.get('end') or start)

        # Applying SQL request
        query = func(*args, **kwargs)

        # Creating json data
        json_objects = simplejson.dumps([item for item in query])

        json_data = json.loads(json_objects)

        # Creating list and fill it by objects
        data = []
        try:
            for i in range(start, end):
                data.append(json_data[i])
        except IndexError as i:
            print(i)

        return JsonResponse(
            {
                'products': data,
                'length': len(json_data),
            },
        )

    return wraps


@response_api
def sales_hits(request):
    """ Function responsible for section 'sales hits'. """

    query = Products.objects.select_related().values(
            'productsdescription__product_name',
            'productsdescription__product_images',
            'product_price',
            'slug',
        ).filter(productsdescription__product_is_hit=True).distinct()

    return query


@response_api
def get_products(request):
    """ Function responsible for section 'all products'. """

    query = Products.objects.select_related().values(
        'productsdescription__product_name',
        'productsdescription__product_images',
        'product_price',
        'slug',
    ).distinct()

    return query


class ProductCard(DetailView):
    model = Products
    template_name = 'shopper/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['product'] = self.get_queryset()

        return context

    def get_queryset(self):
        return Products.objects.filter(slug=self.kwargs['product_slug']).select_related().values(
            'product_price',
            'product_quantity',
            'product_code',
            'product_rating',
            'productsdescription__product_name',
            'productsdescription__product_images',
            'productsdescription__product_model',
            'productsdescription__product_size',
            'productsdescription__seasons',
            'productsdescription__manufacturer',
            'productsdescription__main_material',
            'productsdescription__sole_thickness',
            'productsdescription__type_of_sole',
            'productsdescription__product_other_attrs',
        )










