from django.shortcuts import render, redirect # FBV
from django.views.generic import ListView, DetailView, CreateView # CBV
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category #모델 사용

# Create your views here.

class PostCreate(LoginRequiredMixin,UserPassesTestMixin,CreateView): # Form 모델명_form.html
    model = Post # post_list 변수
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', 'tags']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_vaild(self,form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            #not tag
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

# CBV
class PostList(ListView): # 모델명_list.html
    model = Post # post_list 변수
    ordering = '-pk' # pk 역순으로 나열

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all() # 카테고리 테이블 전체를 categories 변수로 넘김
        context['no_category_post_count'] = Post.objects.filter(category=None).count() # 카테고리가 없는 Post 개수를  no_cate~ 변수로 넘김
        return context # post_list.html로 {post_list, categories, no_category_post_count}


    # template_name = 'blog/blog_list.html' # 템플릿 지정: 기본 템플릿 post_list.html이 아닌 blog_list.html 사용
    # html에서 post_list로 모델값 불러옴



class PostDetail(DetailView): # 모델명_detail.html
    model = Post # post_list 변수

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all() # 카테고리 테이블 전체를 categories 변수로 넘김
        context['no_category_post_count'] = Post.objects.filter(category=None).count() # 카테고리가 없는 Post 개수를  no_cate~ 변수로 넘김
        return context # post_detail.html로 {post, categories, no_category_post_count}

    # template_name = 'blog/single_post_page.html'  # 템플릿 지정: 기본 템플릿 post_detail.html이 아닌 single_post_page.html 사용
    # html에서 post로 모델값 불러옴



def category_page(request, slug):

    if slug == 'no_category':
        category = "미분류"
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )

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