from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing), # 해당 앱의 views.py의 landing 함수로 연결
    path('about_me/',views.about_me), # 해당 앱의 views.py의 about_me 함수로 연결
    path("blog/", include('blog.urls')), # blog app의 urls.py로 연결
]