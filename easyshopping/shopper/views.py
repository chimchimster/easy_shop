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
            'productsdescription__p_name',
            'productsdescription__p_images',
        ).filter(productsdescription__p_is_hit=True)

        context['is_sale'] = Products.objects.select_related().values(
            'productsdescription__p_name',
            'productsdescription__p_images',
        ).filter(productsdescription__p_is_on_sale=True)

        return context

def sales_hits(request):
    """ API responsible for section of sales hits """

    start = int(request.GET.get('start') or 2)
    end = int(request.GET.get('end') or (start + 9))

    query = Products.objects.select_related().values(
            'productsdescription__p_name',
            'productsdescription__p_images',
        ).filter(productsdescription__p_is_hit=True)

    json_objects = simplejson.dumps([item for item in query])


    # Create list and fill it by objects
    data = []
    try:
        for i in range(start, end+1):
            data.append(json.loads(json_objects)[i])
    except IndexError:
        pass

    return JsonResponse(
        {'products': data,}
    )
