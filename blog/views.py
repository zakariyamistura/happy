
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

def main(request):
    posts = Blog.objects.all()
    return render(request, 'index.html',  {'posts': posts})

def detail(request, note_id):
    post = get_object_or_404(Blog, id=note_id)
    return render(request, "detail.html", {'post': post})

def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Blog.objects.create(title=title, content=content)
        return redirect("main")
    return render(request, 'detail.html')

def delete_nnote(request, note_id):
    post = get_object_or_404(Blog, id=note_id)
    post.delete()
    return redirect("main")

def edit_note(request, note_id):
    post = get_object_or_404(Blog, id=note_id)
    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()
        return redirect("main")
    return render(request, 'detail.html', {"post": post})

