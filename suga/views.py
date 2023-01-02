from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from suga.models import *
from suga.models import *
from suga.forms import *

PAGINATION_LIMIT = 4
# Create your views here.

def eagle(request):
    if request.method == 'GET':
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))
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


def products_view(request):
    if request.method == "GET":
        category_id = request.GET.get('category_id')
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if category_id:
            products = Product.objects.filter(category__in=[category_id])
        else:
            products = Product.objects.all()


        if search_text:
            products = products.filter(title__icontains=search_text)



        products = [{
            "id": product.id,
            "title": product.title,
            "description": product.description,
            "price": product.price,
            "category": product.category
        } for product in products]

        max_page = round(products.__len__() / PAGINATION_LIMIT)
        products = products[PAGINATION_LIMIT * (page-1):PAGINATION_LIMIT * page]


        data = {
            'products':products,
        }

        return render(request, "product/product.html", context=data)


def category_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

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





