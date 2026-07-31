"""
URL configuration for p1 project.

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
from os import name
from django.contrib import admin
from django.urls import path,include
from a1 import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"stu",views.seri)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_view,name="login"),
    path("home/",views.home,name="home"),
    path("logout/",views.logout_view,name="logout"),
    path("form",views.form1,name="form"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("edit/<int:id>/",views.edit,name="edit"),
    path("api/",include(router.urls))
    ]
