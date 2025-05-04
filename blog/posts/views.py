from django.shortcuts import render, redirect
from .models import Post

def index(request):
    kiry = Post.objects.all()  # Получить все записи
    
    return render(request, 'posts/index.html', {'eee': kiry})

def new_post(request):
    return render(request, 'posts/new_post.html')

def page_10(request):
    return render(request, 'posts/10.html')

def create_post(request):
    red = request.POST.get('title')
    green = request.POST.get('full_text')
    Post.objects.create(title=red, full_text=green)
    
    return redirect('index')

    # return render(request, 'posts/index.html')