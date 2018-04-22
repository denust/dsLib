# This is our main website paths
# here we say ok, if the website is www.reddit.com/article/ then go to article folder and look in urls.py to see what to do
# about admin we can talk later


from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', include('article.urls')),

]
