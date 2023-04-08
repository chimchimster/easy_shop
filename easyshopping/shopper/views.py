from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Good, Shop, User
from .forms import SearchForm, LoginForm, RegistrationForm


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

        # Query contains shop details
        context['shop'] = get_object_or_404(Shop.objects.filter(slug=self.kwargs['shop_slug']))

        # Query contains goods related to shop
        context['goods'] = Good.objects.select_related('shop').filter(shop__slug=self.kwargs['shop_slug'])

        return context


class UserLogin(LoginView):
    form_class = LoginForm
    template_name = 'shopper/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Авторизация'

        return context

    def get_success_url(self):
        return reverse_lazy('index')


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'shopper/register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'

        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('login')
