
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login 
from django.contrib import messages
from django.shortcuts import render, redirect


def land(request):
    posts = Blog.objects.all() 
    return render(request, 'landing.html', {'posts': posts})

@login_required
def main(request):
    user = request.user
    posts = Blog.objects.filter(user=user)
    return render(request, 'index.html',  {'posts': posts})


def detail(request, note_id):
    post = get_object_or_404(Blog, id=note_id)
    return render(request, "detail.html", {'post': post})


@login_required
def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = request.user
        Blog.objects.create(title=title, content=content, user=user)
        return redirect("main")
    return render(request, 'detail.html')


def delete_nnote(request, note_id):
    post = get_object_or_404(Blog, id=note_id)
    post.delete()
    return redirect("main")


@login_required
def edit_note(request, note_id):
    post = get_object_or_404(Blog, id=note_id)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("main")
    return render(request, 'detail.html', {"post": post})

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            return redirect("login")
    return render(request, 'login.html')

def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.create(username=username, email=email)
            user.set_password(password1)
            user.save()
            login(request, user)
            return redirect("main")
    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return redirect("")



