from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from .models import Blog


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "blog/index.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "blog/contact.html", {})


def element_view(request, *args, **kwargs):
    return render(request, "blog/elements.html", {})


def archive_view(request, *args, **kwargs):
    return render(request, "blog/archive.html", {})


def single_blog_view(request, *args, **kwargs):
    return render(request, "blog/single-blog.html", {})


def category_view(request, *args, **kwargs):
    return render(request, "blog/category.html", {})
