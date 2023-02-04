from pdb import post_mortem
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from .models import *
from .forms import UserRegisterForm, PostForm

html_base = """
    <h1>English Bootcamp Academy</h1>
    <ul>
        <li><a href="/">Homepage</a></li>
        <li><a href="/about">About...</a></li>
        <li><a href="/portfolio">Portfolio</a></li>
        <li><a href="/contact">Contact Us...</a></li>
        
    </ul>
"""
# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def feed(request):
	posts = Post.objects.all()

	context = { 'posts': posts}
	return render(request, 'core/feed.html', context)

def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    return render(request, "core/profile.html"), {'user':user}

def register(request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} created')
            return redirect(to='home')
    else:
        form = UserRegisterForm()
    
    data = {'form' : form}
    return render(request, "registration/register.html", data)

@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Success')
			return redirect('feed')
	else:
		form = PostForm()
	return render(request, 'core/post.html', {'form' : form })

def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'core/profile.html', {'user':user, 'posts':posts})


def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'You`re following {username}')
	return redirect('feed')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'You`re not following {username}')
	return redirect('feed')