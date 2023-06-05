from django.urls import path, include
from . import views

urlpatterns = [
    # CBV
    path('',views.PostList.as_view()), # 해당 앱의 PostList Class로 연결
    path('<int:pk>/',views.PostDetail.as_view()), # 해당 앱의 PostDetail Class로 연결, url의 숫자(e.g, blog/1) pk로 인식
    path('category/<str:slug>/',views.category_page), #FBV
    path('create_post/', views.PostCreate.as_view()), # /blog/create_post/
    path('update_post/<int:pk>/', views.PostUpdate.as_view()), # /blog/update_post/5
    path('<int:pk>/new_comment/', views.new_comment),



    # FBV
    # path('', views.index), # 해당 앱의 index 함수로 연결
    # path('<int:pk>/',views.single_post_page), # 해당 앱의 single_post_page 함수로 연결, url의 숫자(e.g, blog/1) pk로 인식
]