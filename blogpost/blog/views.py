from django.shortcuts import render
from .models import *
# from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all(),
        'is_loggedin': request.user.is_authenticated
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {
        'title': 'About'
    })