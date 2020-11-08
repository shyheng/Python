from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# ur映射（地址

def index(reguest):
    products = Product.objects.all()
    return HttpResponse("hello world")


def new(reguest):
    return HttpResponse('New Products')


