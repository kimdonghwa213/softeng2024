from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
        path('<int:pk>/', views.single_post_page, name='single_post_page'),
        path('blog/', views.blog, name='blog'),
        path('', views.index, name='index'),
        path('about_me/', views.about_me, name='about_me'),
        path('career/', views.career, name='career'),
]