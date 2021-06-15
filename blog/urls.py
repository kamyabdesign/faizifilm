from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blogs'),
    path('post_detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search, name='search'),
    path('tag/<slug:tag>/', views.blog_tag, name='tag'),
    path('category/<slug:category>/', views.blog_category, name='category'),
]
