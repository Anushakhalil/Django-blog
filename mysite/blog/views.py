from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from .models import Blog

from blogger.models import Blogger

from .forms import BlogModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home_view(request, *args, **kwargs):


    print(len(Blog.objects.all()))
    return render(request, "blog/index.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "blog/contact.html", {})


def element_view(request, *args, **kwargs):
    return render(request, "blog/elements.html", {})


def archive_view(request, *args, **kwargs):
    objs = Blog.objects.all()
    context = {
        "objs":objs
    }

    return render(request, "blog/archive.html", context)


def single_blog_view(request, my_id, *args, **kwargs):
    
    # obj = Blog.objects.get(id = my_id)
    obj = get_object_or_404(Blog, id = my_id)

    return render(request, "blog/single-blog.html", {"obj": obj})

def category_details_view(request, catName, *args, **kwargs):

    objlist = Blog.objects.all()
    catList = []
    for i in objlist:
        if i.cat == catName:
            catList.append(i)
    print(catList)

    return render(request, "blog/category_details.html", {"objs":catList})


def category_view(request, *args, **kwargs):

    catList = []
    for i in Blog.categories:
        catList.append(i[1])
    return render(request, "blog/category.html", {"cats": catList})

@login_required(login_url='login')
def create_view(request, *args, **kwargs):
    form = BlogModelForm(request.POST, request.FILES)

    # if request.user.is_authenticated:
    # form.fields['blogger'] = str(request.user)

    

    if form.is_valid():
        # 

        # from datetime import datetime
        # now = datetime.now()
        # form.date = str(now.strftime("%m/%d/%Y"))
        # form.time = str(now.strftime("%H:%M:%S"))
        # print("SAVE HOGYAAAAAAAAAAA")

        

        form.save()

        a = Blog.objects.get(id = len(Blog.objects.all()))
        a.blogger = str(request.user)
        a.save()
        return redirect('archive')
        # form = BlogModelForm()
        # mod = Blog.objects.get(pk = self.id)
        # mod.picture = form.cleaned_data["picture"]
        # mod.save()

    context = {
        "title": form.fields['title'],
        "picture": form.fields['picture'],
        "content": form.fields['content'],
        "cat": form.fields['cat']
    }
    return render(request, "blogs/index.html", context)

# from django.views.generic import (
#     CreateView)

# class create_view(CreateView):
#     template_name = 'blogs/create_blog.html'
#     form_class = BlogModelForm
#     queryset = Blog.objects.all()