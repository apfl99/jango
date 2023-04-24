from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('list/',views.list),
    path('list/<int:pk>/',views.name_card),
    path('list/<int:pk>/alter/',views.name_card2),

]