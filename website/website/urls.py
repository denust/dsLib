

from django.contrib import admin
from django.urls import path, include
from . import views

# Markdown stuff
from django.conf.urls import url
from markdownx import urls as markdownx
# Markdown stuff

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', include('article.urls')),
    path('', views.index, name='index'),
	url(r'^markdownx/', include(markdownx)), # need this for markdown to work
]
