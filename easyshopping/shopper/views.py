from django.contrib.auth import logout
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