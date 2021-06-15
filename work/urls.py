from django.urls import path
from . import views


urlpatterns = [
    path('', views.working, name="work"),
    path('work_detail/<slug:slug>/', views.work_detail, name="work_detail"),
    path('category/<slug:category>/', views.work_category, name='work_category'),

]
