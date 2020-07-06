


from django.contrib import admin
from django.urls import path, include
from blog.views import (home_view, contact_view, single_blog_view,element_view,category_view, archive_view, create_view, category_details_view)

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('blog/<int:my_id>/', single_blog_view, name='blogDetails'),
    path('elements/', element_view, name='elements'),
    path('category/', category_view, name='category'),
    path('archive/', archive_view, name='archive'),
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('create/', create_view, name="create"),
    path('', include('blog.urls')),
    # path('category/', include(blo))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
