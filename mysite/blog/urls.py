from django.urls import path, include

from .views import single_blog_view

app_name = "Blog"
urlpatterns = [
    path('<int:my_id>/', single_blog_view, name='blogDetails'),
]
