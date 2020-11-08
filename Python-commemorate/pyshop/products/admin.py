from django.contrib import admin
from .models import Product, Off

class OfferAdmin(admin.ModelAdmin):
    list_display = ('我','爱')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('名字','不知道','额')

admin.site.register(Off, OfferAdmin)
admin.site.register(Product,ProductAdmin)
