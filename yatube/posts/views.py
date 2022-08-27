from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:10]
    context = {
        'title': title,
        'posts': posts}

    return render(request, template, context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {slug}'
    posts = group.posts.all()[:10]
    template = 'posts/group_list.html'
    context = {
        'title': title,
        'group': group,
        'posts': posts}
    return render(request, template, context)
