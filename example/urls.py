"""
URL configuration for example project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import ProductListAPI
from student.views import SignUpAPI, SignInAPI, LessonInfoListAPI, LessonInfoCreateAPI, LessonCreateAPI, LessonMonthlyAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', ProductListAPI.as_view()),
    path('api/student/sign-up', SignUpAPI.as_view()),
    path('api/student/sign-in', SignInAPI.as_view()),
    path('api/lesson-info/list', LessonInfoListAPI.as_view()),
    path('api/lesson-info/create', LessonInfoCreateAPI.as_view()),
    path('api/lesson/create', LessonCreateAPI.as_view()),
    path('api/lesson/monthly', LessonMonthlyAPI.as_view()),
]