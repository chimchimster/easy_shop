from .views import IndexView, ShopView
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/<slug:shop_slug>', ShopView.as_view(), name='shop'),

]