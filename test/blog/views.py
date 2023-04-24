from django.shortcuts import render # FBV
from django.views.generic import ListView, DetailView # CBV
from .models import Post #모델 사용

# Create your views here.

# 08 웹 페이지 만들기

# CBV
class PostList(ListView): # 모델명_list.html
    model = Post # post_list 변수
    ordering = '-pk' # pk 역순으로 나열
    template_name = 'blog/blog_list.html' # 템플릿 지정: 기본 템플릿 post_list.html이 아닌 blog_list.html 사용
    # html에서 post_list로 모델값 불러옴

class PostDetail(DetailView): # 모델명_detail.html
    model = Post # post_list 변수
    template_name = 'blog/single_post_page.html'  # 템플릿 지정: 기본 템플릿 post_detail.html이 아닌 single_post_page.html 사용
    # html에서 post로 모델값 불러옴

# FBV
# def index(request):
#     posts = Post.objects.all().order_by('-pk') # Post 모델값 pk 역순으로 가져옴
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts # posts로 렌더링
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk) # pk 매개변수로 받아서, pk에 해당하는 값 가져옴
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post, # post로 렌더링
#         }
#     )