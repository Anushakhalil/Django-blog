"""untitled1 URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home_view,contact_view,product_list_view,  single_blog_view, about_view, blog_view, product_list_view, single_list_view, login_view, checkout_view, cart_view, confirmation_view, elements_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path('about/', about_view, name='about'),
    path('blog/',blog_view, name='blog'),
    path('product-list/', product_list_view, name='product_list'),
    path('single-product/', single_list_view, name='single-product'),
    path('login/', login_view, name='login'),
    path('checkout/', checkout_view, name='checkout'),
    path('cart/', cart_view, name='cart'),
    path('confirmation/',confirmation_view, name='confirmation' ),
    path('elements/', elements_view, name='elements'),
    path('single-blog/', single_blog_view, name='single-blog'),
    path('contact/', contact_view, name='contact'),
    path('product-list/', product_list_view, name='product_list'),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
