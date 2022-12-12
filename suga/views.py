from django.shortcuts import render
from django.http import HttpResponse
import datetime


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
