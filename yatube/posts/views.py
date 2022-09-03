from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Group, User
from django.core.paginator import Paginator
from .forms import PostForm
from django.contrib.auth.decorators import login_required

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

@login_required
def post_create(request):
    template = 'posts/create_post.html'

    current_user = request.user.username

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # text = form.cleaned_data['text']
            # group = form.cleaned_data['group']
            event = form.save(commit=False)
            event.author = request.user
            event.save()

            return redirect(f'/profile/{current_user}/')

        return render(request, template, context)


    form = PostForm()

    context = {
        'form': form,
    }

    return render(request, template, context)

def post_edit(request, post_id):

    template = 'posts/create_post.html'
    form = PostForm(request.GET)
    is_edit = True
    context = {
        'form':form,
        'is_edit':is_edit,
    }
    return render(request, template, context)