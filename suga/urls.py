from django.contrib import admin
from django.urls import path
from suga.views import *

urlpatterns = [
    path('product/', product_view),
    path('/', main_view),
    ]