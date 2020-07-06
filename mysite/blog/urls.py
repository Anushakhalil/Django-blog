from django.urls import path, include

from .views import single_blog_view, category_details_view

app_name = "Blog"
urlpatterns = [
    path('blog/<int:my_id>/', single_blog_view, name='blogDetails'),
    path('category/<str:catName>', category_details_view, name="catDetails")
]
