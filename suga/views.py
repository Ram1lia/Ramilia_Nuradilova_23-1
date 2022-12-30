from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from suga.models import *
from suga.models import *
from suga.forms import *

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
       products = Product.objects.all()
       # jk={
       #     'product':gg
       # }
       return render(request,'product/product.html',{'products':products})


def category_view(request):
    if request.method == 'GET':
        category = Category.objects.all()

        return render(request,'product/categories.html', {'category':category})


def product_detail_view(request, id):
    if request.method == 'GET':
        gg = Product.objects.get(id=id)
        jk = {
            'product': gg,
            'review': gg.review.all()
        }

        return render(request, 'product/product_detail.html', context=jk)

def productcreateview(request):
    if request.method == 'GET':
        sg = {
            'form': ProductCreateForm

        }
        return render(request, 'product/create.html', context=sg)
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                author_id=1,
                title=form.cleaned_data.get('title'),
                price=form.cleaned_data.get('price'),
                text=form.cleaned_data.get('text'),

            )

            return redirect('/product')
        else:
            data = {
                'form': form
            }
            return render(request, 'product/create.html', context=data)





