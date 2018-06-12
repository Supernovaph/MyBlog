from django.contrib import admin
from .models import Product, Order



@admin.register(Product)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class AuthorAdmin(admin.ModelAdmin):
    pass    