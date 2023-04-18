from django.contrib.auth.admin import UserAdmin

from .models import ShopperUser, OrdersStatus, OrderItems, Orders, ProductsDescription, ProductsTypes, Products, Category, Comment, ImageProduct
from .forms import UserCreationForm, RegistrationForm

from django.contrib import admin


class ShopperUserAdmin(UserAdmin):
    form = UserCreationForm
    model = ShopperUser
    list_display = ['username', 'email']


class CommentAdmin(admin.ModelAdmin):
    readonly_fields  = ('date_created', 'date_edited')

admin.site.register(ShopperUser, ShopperUserAdmin)
admin.site.register(OrdersStatus)
admin.site.register(OrderItems)
admin.site.register(Orders)
admin.site.register(ProductsDescription)
admin.site.register(ProductsTypes)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ImageProduct)