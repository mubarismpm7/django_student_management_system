"""
URL configuration for studentproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from studApp import views
from rest_framework.authtoken import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user',views.UserCreate.as_view(),name="user_create"),
    path('token',auth_view.obtain_auth_token),
    path('student/',views.StudentCreate.as_view(),name="create_student"),
    path('student/<int:pk>', views.StudentDetail.as_view(),name="updateretrievedelete"),
]
