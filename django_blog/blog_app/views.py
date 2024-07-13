from django.shortcuts import render
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Posts'
    }
    return render(request, 'blog_app/index.html', context)

def about(request):
    return render(request, 'blog_app/about.html', {'title': 'About'})
