from django.contrib import admin
from django.urls import path
from users.views import *


urlpatterns = [
    path('users/login/', login_view),
    path('users/logout/', logout_view),
    path('users/register/', register_view ),
    ]