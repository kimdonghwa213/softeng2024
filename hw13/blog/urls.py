from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view(), name='post_list'),
    # path('<int:pk>/', views.single_post_page),
    # path('', views.index),
]