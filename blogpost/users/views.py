from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from blog.models import Post

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Proceed to log in, please.')
            return redirect('login')
    else:    
        form = UserRegisterForm()
    return render(request, 'users/register.html', {
        'form': form,
        'title': 'Register'
    })


@login_required
def profile(request, user_id):
    author = User.objects.get(id=user_id)
    context = {
        'title': request.user.username,
        'posts': Post.objects.filter(author_id=author.id).all(),
        'author': author
    }
    return render(request, 'users/profile.html', context)