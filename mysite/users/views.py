from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                # messages.success(request, 'This is the account for' + user)
                return redirect('login')

    context = {'form': form}
    return render(request, "users/signup.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            # else:
            #     messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, "users/login.html", context)


# @login_required(login_url='login')  # ye restrict krne kay liye hai
# def logoutPage(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect('login')
#     context = {}
#     return render(request, "users/dashboard.html", context)
