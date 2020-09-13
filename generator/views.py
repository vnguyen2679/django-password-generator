from django.shortcuts import render
import random

# Create your views (pages) here.

def home(request):
    return render(request, 'generator/home.html', {'password': '123456789'})

def password(request):    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    password = ''
    for __ in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})

def about(request):
    return render(request, 'generator/about.html', {'designer': 'Vincent Nguyen', 'year': 2020})
