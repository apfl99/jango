from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

# 08 웹 페이지 만들기 - CBV로 페이지 만들기 참조 CLASS 방식
class PostList(ListView): # 모델명_list.html
    model = Post # post_list 변수
    ordering = '-pk'
    template_name = 'blog/blog_list.html' # 템플릿 지정

class PostDetail(DetailView): # 모델명_detail.html
    model = Post # post_list 변수
    template_name = 'blog/single_post_page.html'  # 템플릿 지정


# 함수 방식

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post,
#         }
#     )