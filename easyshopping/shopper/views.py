from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Good, Shop


class IndexView(ListView):
    """ Describes all shops page """

    # Define a model and template which must be rendered
    model = Shop
    template_name = 'shopper/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # Retrieves context
        context = super().get_context_data(**kwargs)

        # Add query items to context
        context['shops'] = self.get_queryset()

        return context

    def get_queryset(self):
        return Shop.objects.all()


class ShopView(DetailView):
    """ Describes each unique shop """

    # Define model, template and slug for URL
    model = Shop
    template_name = 'shopper/shop.html'
    slug_url_kwarg = 'shop_slug'
    context_object_name = 'shop'

    def get_context_data(self, **kwargs):
        # Retrieves context
        context = super().get_context_data(**kwargs)
        print(context)

        # Add query items to context
        context['shop'] = self.get_queryset()

        return context

    def get_queryset(self):
        return Shop.objects.filter(slug=self.kwargs['shop_slug'])