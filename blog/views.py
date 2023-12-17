import random
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import path, include
# redirect 함수는 함수에 전달된 값을 참고하여 페이지 이동을 수행
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator

from django.contrib import auth
from django.contrib.auth.models import User  # User 모델을 사용하기 위해 import
from django.contrib.auth import authenticate, login, logout  # type: ignore
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt  # csrf 이슈때문에 csrf_exempt를 사용

from django.core.paginator import Paginator


def main(request):
    return render(request, 'index.html')
