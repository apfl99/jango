from django.shortcuts import render, redirect # FBV

from django.views.generic import ListView, DetailView, CreateView, UpdateView # CBV
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category, Comment #모델 사용
from .forms import CommentForm # CommentForm
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk) # 객체 확인

        # post 형식이면 파이썬 형식으로 form 만들고 저장
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url()) # 작성 후 댓글 링크
        else:
            return redirect(post.get_absolute_url()) # get이면 그냥 detail링크

    else:
        raise PermissionDenied


def delete_comment(request,pk):
    comment = get_object_or_404(Comment, pk=pk) # 객체 확인
    post = comment.post

    # 본인 인증 후 삭제
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm # UpdateView

    # template_name = comment_form.html

    # request와 response 중개자 역할 => 여기서는 작성자 본인 인증 후, 업데이트 진행
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


def csrf_failure(request, reason=""):
    return redirect('/blog/')

class PostUpdate(LoginRequiredMixin, UpdateView): # Form 모델명_form.html => Create와 똑같음
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', 'tags']

    template_name = "blog/post_update_form.html" # create와 같은 form이므로 Set

    # request와 response 중개자 역할 => 여기서는 작성자 본인 인증 후, 업데이트 진행
    def dispatch(self, request, *args, **kwargs): # 기존 값들 불러옴
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): # Form 모델명_form.html
    model = Post # post_list 변수
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', 'tags']


    # 권한 관리
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    # form_valid : 유효한 폼 데이터 처리 로직
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user # author 오버라이딩
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

# CBV
class PostList(ListView): # 모델명_list.html
    model = Post # post_list 변수
    ordering = '-pk' # pk 역순으로 나열
    paginate_by = 2 # 페이지네이션 2개씩 설정

    # CBV의 경우 context에 넣어서 html로 변수 넘겨줌
    # get_context_data(self, **kwargs):
    #   context = super(자신의 인스턴스, self).get_context_data()로 클래스형 view 인스턴스를 넣어주고 시작
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data() # 클래스형 view 인스턴스를 넣어주고 시작: 오버라이딩
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
        context['comment_form'] = CommentForm # forms.py에서 불러옴 => Comment 모델 content 저장
        return context # post_detail.html로 {post, categories, no_category_post_count, comment_form}

    # template_name = 'blog/single_post_page.html'  # 템플릿 지정: 기본 템플릿 post_detail.html이 아닌 single_post_page.html 사용
    # html에서 post로 모델값 불러옴

class PostSearch(PostList):
    paginate_by = None # 페이지네이션 하지 않음

    # 동적 쿼리 사용
    def get_queryset(self):
        q = self.kwargs['q']
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(tags__name__contains=q)
        ).distinct() # 중복 제거
        return post_list

    # context Data Set
    def get_context_data(self, **kwargs): # 위에 따로 띄워주기 위한 Text 만들기
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'
        return context



def category_page(request, slug):

    if slug == 'no_category':
        category = "미분류"
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)



    return render(
        request,
        'blog/post_list.html', # post_list로 렌더링
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