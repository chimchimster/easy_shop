from .views import IndexView, ShopView, UserLogin, logout_user, RegisterUser
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('shop/<slug:shop_slug>', ShopView.as_view(), name='shop'),
    path('login', UserLogin.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),

]