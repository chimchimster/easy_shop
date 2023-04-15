from django.templatetags.static import static
from django.urls import path
from .views import IndexView, sales_hits, get_products

urlpatterns = [
    path('',  IndexView.as_view(), name='index'),

    # API routes
    path('sales_hits', sales_hits),
    path('all_products', get_products)
]