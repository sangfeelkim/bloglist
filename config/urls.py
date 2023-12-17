from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from django.urls import re_path

# app_name = 'config' 이걸 무한반복이 된다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
