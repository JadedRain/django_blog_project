from django.shortcuts import render

posts = [
    {
        'author': 'JadedRain',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'Now'
    },
        {
        'author': 'Deserted',
        'title': 'Post 2',
        'content': 'Joel a nerd',
        'date_posted': 'Now'
    },
]


def index(request):
    context = {
        'posts': posts,
        'title': 'Posts'
    }
    return render(request, 'blog_app/index.html', context)

def about(request):
    return render(request, 'blog_app/about.html', {'title': 'About'})
