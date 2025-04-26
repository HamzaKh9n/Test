from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        s = blog_details.objects.filter(
            Q(name__icontains = search)|Q(title__icontains = search)|Q(content__icontains = search)
        )
    
    else:
        s = blog_details.objects.all()
    return render(request , 'home.html' , {'s':s})

def bform(request):
    if request.method == 'POST':
        blog_details.objects.create(
            name = request.POST.get('name'),
            title = request.POST.get('title'),
            author = request.user,
            image = request.FILES.get('img'),
            content = request.POST.get('text'),
            time = datetime.datetime.now()
        )
    return render(request , 'blogform.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request ,username=username, email=email , password=password)
        if user is not None:
            auth.login(request , user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is incorrect')
    return render(request, 'Auth/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=username,email=email , password=password)
        user = authenticate(request ,username=username, email=email , password=password)
        if user is not None:
            auth.login(request , user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'Auth/signup.html')


def out(request):
    auth.logout(request)
    return redirect('login')

