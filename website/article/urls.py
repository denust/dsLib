from django.urls import path, include
from . import views
from django.conf.urls import url
from markdownx import urls as markdownx




urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.get_article, name = 'get_article'), 
    ]