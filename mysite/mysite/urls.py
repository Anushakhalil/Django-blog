"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from blog.views import (home_view, contact_view, single_blog_view,element_view,category_view, archive_view, create_view)

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('blog/<int:my_id>/', single_blog_view, name='blogDetails'),
    path('elements/', element_view, name='elements'),
    path('category/', category_view, name='category'),
    path('archive/', archive_view, name='archive'),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('create/', create_view, name="create")
]
