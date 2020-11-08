from django.urls import path
from .import views  #用.引入views

# /削减
urlpatterns = [
    path('',views.index),
    path('new',views.new)
]