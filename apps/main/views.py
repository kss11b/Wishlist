from django.shortcuts import render, redirect, HttpResponse
from .models import User, Wish
import bcrypt, time
from datetime import datetime, date
from django.contrib import messages
def index(request):

    return render(request, 'main/index.html')

def success(request):
    return render(request, 'main/success.html')

def create(request):
    if User.objects.registration(request.POST):

        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], date_hired=request.POST['date_hired'], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
    else:
        messages.error(request, "Registration Error")

    return redirect('/')

def login(request):
    if User.objects.login(request.POST):
        identify = User.objects.get(email=request.POST['email_login'])
        request.session['id'] = identify.id
        request.session['first_name'] = identify.first_name
        return redirect('/success')
    else:
        messages.error(request, "Login Error")
        return redirect('/')

def new_product(request, id):

    return redirect('/success')

def new_product_page(request):

    return render(request, 'main/appointments.html')

def delete(request):
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')
