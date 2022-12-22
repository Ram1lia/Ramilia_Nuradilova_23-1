from django.contrib import admin
from django.urls import path
from suga.views import *
from django.conf.urls.static import static
from djangoProject import settings


urlpatterns = [
    path('product/', product_view),
    path('product/<int:id>', product_detail_view),
    path('/', main_view),
    path('categories/', category_view),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)