import json

import simplejson
from django.contrib.auth import logout
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from .models import ProductsDescription, Products, Comment
from .forms import ReviewFrom


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

def response_api_card_item(func):

    def wraps(*args, **kwargs):

        query = func(*args, **kwargs)

        json_objects = simplejson.dumps([item for item in query])

        json_data = json.loads(json_objects)

        return JsonResponse(
            {'items': json_data}
        )

    return wraps



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




