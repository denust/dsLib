from django.urls import path
from . import views

# Here we say which views to use at which paths. Mind all of this pages already start with www.reddit.com/article/ because
# its the name of this app/module


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.get_article, name = 'get_article')  # this is a cool way of getting a stored variable
    # in path, instead of .../article?id=1234 we will have .../article/1234/ but we can do other way as well
]