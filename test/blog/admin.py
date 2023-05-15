from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.
admin.site.register(Post) # 만든 모델 등록

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )} # name 필드값으로 slug를 자동생성하도록 설정

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )} # name 필드값으로 slug를 자동생성하도록 설정

admin.site.register(Category,CategoryAdmin) # 만든 모델 등록
admin.site.register(Tag,TagAdmin) # 만든 모델 등록