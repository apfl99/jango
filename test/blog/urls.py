from django.urls import path, include
from . import views

urlpatterns = [
    # class방식
    path('',views.PostList.as_view()),
    path('<int:pk>/',views.PostDetail.as_view()),

    # 함수 방식
    # path('', views.index),
    # path('<int:pk>/',views.single_post_page),
]