from django.shortcuts import render
from django.http import HttpResponse
import datetime
from suga.models import *

# Create your views here.

def eagle(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def goodby(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user!")


def wings(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now().date())

def main_view(request):
    if request.method == 'GET':
        return render(request,'layouts/index.html')

def product_view(request):
    if request.method == 'GET':
       gg = Product.objects.all()
       jk={
           'product':gg
       }
       return render (request,'product/product.html',context=jk)


def product_detail_view(request, id):
    if request.method == 'GET':
        gg = Product.objects.get(id=id)
        jk = {
            'product': gg,
            'review': gg.review.all()
        }

        return render(request, 'product/product_detail.html', context=jk)

