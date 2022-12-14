from django.shortcuts import render,redirect
from users.forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from users.utils import get_user_form_request
from django.views.generic import ListView, CreateView, DetailView

def login_view(request):
    if request.method == 'GET':
        data = {
            'form': LoginForm,
        }
        return render(request, 'users/login.html', context=data)

    if request.method == 'POST':
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = authenticate (
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user:
                login(request, user)
                return redirect('/product')

            else:
                form.add_error('username', 'bad request')
        data = {
            'form': form
        }
        return render(request, 'users/login.html', context=data)


def logout_view(request):
    logout(request)
    return redirect('/product')


def register_view(request):
    if request.method == 'GET':
        data = {
            'form': RegisterForm,
        }

        return render(request, 'users/register.html', context=data)

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password1') == form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1')
                )

                login(request, user)
                return redirect('/product')
            else:
                form.add_error('password1', 'password do not match!')

        data = {
            'form': form


        }
        return render(request, 'users/register.html', context=data)

