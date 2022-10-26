from django.shortcuts import render, get_object_or_404

from .models import Group, Post

POST_PAGES = 10


def index(request):
    posts = Post.objects.all()[:POST_PAGES]
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """View-функция для страницы сообщества"""
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POST_PAGES]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
