from django.templatetags.static import static
from django.urls import path
from .views import IndexView, sales_hits, get_products, ProductCard

urlpatterns = [
    path('',  IndexView.as_view(), name='index'),
    path('product/<slug:product_slug>', ProductCard.as_view(), name='product'),

    # API routes
    path('sales_hits', sales_hits),
    path('all_products', get_products),
]