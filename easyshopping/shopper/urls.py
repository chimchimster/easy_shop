from django.urls import path
from .views import IndexView, RegisterUser, LoginUser, sales_hits, get_products, get_pictures, get_comments, ProductCard, activate_email, logout_user

urlpatterns = [
    path('',  IndexView.as_view(), name='index'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('product/<slug:product_slug>', ProductCard.as_view(), name='product'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate_email, name='activate'),

    # API routes
    path('sales_hits', sales_hits),
    path('all_products', get_products),
    path('product_images/<slug:product_slug>', get_pictures),
    path('product_comments/<slug:product_slug>', get_comments),
]