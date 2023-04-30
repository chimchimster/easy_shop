import json

import simplejson
from django.contrib.auth import logout, login, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .models import ProductsDescription, Products, Comment
from .forms import ReviewFrom, RegistrationForm, LoginForm
from .response_apis import response_api, response_api_card_item
from .token import account_activation_token


class IndexView(TemplateView):
    template_name = 'shopper/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class RegisterUser(CreateView):
    form_class = RegistrationForm
    template_name = 'shopper/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # Getting domain of site
        current_site = get_current_site(self.request)

        mail_subject = 'Ссылка для активации отправлена на ваш почтовый адрес'

        message = render_to_string(
            'shopper/account_activate.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

        to_email = form.cleaned_data.get('email')

        email = EmailMessage(
            mail_subject,
            message,
            to=[to_email]
        )

        email.send()

        return HttpResponse('Ссылка для активации отправлена на вашу почту. Пройдите активацию')


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'shopper/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy('index')

@response_api
def sales_hits(request):
    """ Function responsible for section 'sales hits'. """

    query = Products.objects.select_related().filter(imageproduct__default=True).values(
            'productsdescription__product_name',
            'imageproduct__image',
            'product_price',
            'slug',
        ).filter(productsdescription__product_is_hit=True).distinct()

    return query


@response_api
def get_products(request):
    """ Function responsible for section 'all products'. """

    query = Products.objects.select_related().filter(imageproduct__default=True).values(
        'productsdescription__product_name',
        'imageproduct__image',
        'product_price',
        'slug',
    ).distinct()

    return query

@response_api_card_item
def get_pictures(request, product_slug):
    """ Function responsible for loading pictures
        of particular product. """

    slug = request.__dict__['path_info'].lstrip('/product_images/')

    query = Products.objects.filter(slug=slug).select_related().values(
        'imageproduct__image',
        'imageproduct__default',
    )

    return query


@response_api
def get_comments(request, product_slug):
    """ Function responsible for 'comments' section. """

    slug = request.__dict__['path_info'].lstrip('/product_comments/')

    query = Products.objects.filter(slug=slug).select_related().values(
        'comment__content',
    )

    return query


class ProductCard(FormMixin, DetailView):
    model = Products
    form_class = ReviewFrom
    template_name = 'shopper/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['product'] = self.get_queryset()

        context['comment_form'] = ReviewFrom()

        return context

    def get_queryset(self):
        return Products.objects.filter(slug=self.kwargs['product_slug']).select_related().values(
            'product_price',
            'product_quantity',
            'product_code',
            'product_rating',
            'productsdescription__product_name',
            'productsdescription__product_model',
            'productsdescription__product_size',
            'productsdescription__seasons',
            'productsdescription__manufacturer',
            'productsdescription__main_material',
            'productsdescription__sole_thickness',
            'productsdescription__type_of_sole',
            'productsdescription__product_other_attrs',
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():

            comment = Comment.objects.create(
                title='',
                content=form.cleaned_data['body'],
                author_id=request.user,
                product_id=Products.objects.filter(slug=self.kwargs['product_slug'])[0],

            )
            comment.save()

            return HttpResponseRedirect('/product/' + self.kwargs['product_slug'])

        return render(
            request,
            self.template_name,
            {'comment_form': form}
        )


def activate_email(request, uidb64, token):
    User = get_user_model()

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Спасибо за подтверждение! Теперь вы можете войти в свой аккаунт!.')
    else:
        return HttpResponse('Ссылка устарела!')


def logout_user(request):
    logout(request)
    return redirect('login')