from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views  # 현재의 views의 명령어를 실행시킨다.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
# 로그인, 로그아웃, 비밀번호 변경 등의 뷰를 제공하는 라이브러리
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf.urls import include
from django.conf import settings
from .views import *


# 추가 import

from django.contrib.sitemaps.views import sitemap

app_name = 'blog'

urlpatterns = [
    path('', views.main, name='main'),
]
