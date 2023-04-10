from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

# 08 웹 페이지 만들기 - CBV로 페이지 만들기 참조
# class PostList(ListView): # 모델명_list.html
#     model = Post
#     template_name = 'blog/index.html' # 템플릿 지정


def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )