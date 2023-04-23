"""test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 페이지 url
from django.contrib import admin
from django.urls import path, include

# 미디어 파일을 위한 URL 처리
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('single_pages.urls')), # single_pages app의 urls.py로 연결
    path("blog/", include('blog.urls')), # blog app의 urls.py로 연결
]

# 미디어 파일 관리: setting.py의 MEDIA_URL과 MEDIA_ROOT를 활용한 url 설정
# /media로 브라우저가 실행되면, 서버의 _media로 url 설정
# e.g, http://localhost:8000/media/blog/images/2023/04/17/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-04-17_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.32.02.png
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)