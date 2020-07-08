from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, "t/HOME.html",{})

def about_view(request):
    return render(request, "t/about.html",{})

def blog_view(request):
    return render(request, "t/blog.html", {})

def product_list_view(request):
    return render(request, "t/product_list.html", {})

def single_list_view(request):
    return render((request, "t/single-procust.html", {}))

def login_view(request):
    return render(request, "t/login.html", {})

def checkout_view(request):
    return render(request, "t/checkout.html", {})

def cart_view(request):
    return render(request, "t/cart.html", {})

def confirmation_view(request):
    return render(request, "t/contact.html", {})

def elements_view(request):
    return render(request, "t/elements.html", {})

def single_blog_view(request):
    return render(request, "t/single-blog.html", {})

def contact_view(request):
    return render(request, "t/contact.html", {})

def product_list(request):
    return render(request, "t/product_list.html", {})