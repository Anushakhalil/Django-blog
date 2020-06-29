from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from .models import Blog

from .forms import BlogModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "blog/index.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "blog/contact.html", {})


def element_view(request, *args, **kwargs):
    return render(request, "blog/elements.html", {})


def archive_view(request, *args, **kwargs):
    return render(request, "blog/archive.html", {})


def single_blog_view(request, my_id, *args, **kwargs):
    
    obj = Blog.objects.get(id = my_id)

    return render(request, "blog/single-blog.html", {"obj": obj})


def category_view(request, *args, **kwargs):
    return render(request, "blog/category.html", {})

@login_required(login_url='login')
def create_view(request, *args, **kwargs):
    form = BlogModelForm(request.POST)

    if form.is_valid():
        # print("SAVE HOGYAAAAAAAAAAA")
        form.save()
        return redirect(Blog.get_absolute_url)
        # form = BlogModelForm()
        # mod = Blog.objects.get(pk = self.id)
        # mod.picture = form.cleaned_data["picture"]
        # mod.save()

    context = {
        "form": form
    }
    return render(request, "blogs/index.html", context)

# from django.views.generic import (
#     CreateView)

# class create_view(CreateView):
#     template_name = 'blogs/create_blog.html'
#     form_class = BlogModelForm
#     queryset = Blog.objects.all()