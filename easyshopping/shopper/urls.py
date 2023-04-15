from django.templatetags.static import static
from django.urls import path
from .views import IndexView, sales_hits

urlpatterns = [
    path('',  IndexView.as_view(), name='index'),

    # API routes
    path('sales_hits', sales_hits, name='c'),
]