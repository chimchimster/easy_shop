from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Good, Shop


class Index(ListView):
    """ Describes all shops page """

    # Difine a model and template which must be rendered
    model = Shop
    template_name = 'shopper/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # Retrieves context
        context = super().get_context_data(**kwargs)
        context['shops'] = self.get_queryset()
        return context

    def get_queryset(self):
        return Shop.objects.all()
