from django.shortcuts import redirect, render
from django.utils import timezone

from blog.forms import PostForm
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_info(request, title, author):
    post = Post.objects.filter(title=title).first()
    return render(request, 'blog/post_info.html', {'post': post})


def post_new(request):
    if  (str(request.user) == "AnonymousUser"):
        return redirect('/admin/login/?next=/post/new')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', { 'form': form })
