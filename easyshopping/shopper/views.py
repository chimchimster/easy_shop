from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .models import Good, Shop
from .forms import SearchForm, LoginUserForm


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

        # Add search from to context
        context['search'] = SearchForm()

        print(context)

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

        # Add query items to context
        context['shop'] = self.get_queryset().get()

        return context

    def get_queryset(self):
        return Shop.objects.filter(slug=self.kwargs['shop_slug'])


class UserLogin(LoginView):
    form_class = LoginUserForm
    template_name = 'shopper/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Авторизация'

        return context

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')