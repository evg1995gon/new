from django.shortcuts import render, get_object_or_404
from posts.models import Post, Group, User
from django.core.paginator import Paginator

def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': title,
        'posts': posts,
        'page_obj':page_obj,}

    return render(request, template, context)


def group_list(request, slug):

    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {slug}'
    posts = group.posts.all()
    template = 'posts/group_list.html'

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': title,
        'group': group,
        'posts': posts}
    return render(request, template, context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.all()
    #posts = Post.objects.filter(author=user)  #можно и так

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user': user,
        'posts': posts,
        'page_obj':page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):

    post = Post.objects.get(id=post_id)
    lol = post.author
    posts = Post.objects.filter(author=lol)
    title = post.text[0:30]
    context = {
        'posts': posts,
        'post': post,
    }

    return render(request, 'posts/post_detail.html', context)