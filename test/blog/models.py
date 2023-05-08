import os.path

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) # unicode => 한글 허용

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = "Categories" # DB 테이블 명 지정, 원래 Categorys로 설정되어 있음

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) # 새로 작성했을 때 생성
    updated_at = models.DateTimeField(auto_now=True) # 수정했을 때 업데이트

    # author
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #user를 지웠을때, 사용자가 작성한 Post의 author를 NULL로 설정 => none으로 표시
    #on_delete=models.CASCADE #user를 지웠을때, User에 연결되어있는 모든 Post을 지움

    #category
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return  self.get_file_name().split(".")[-1]


