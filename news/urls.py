from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
]
