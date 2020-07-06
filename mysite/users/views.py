from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from blogger.models import Blogger
from blogger.forms import CreateBloggerForm

from django.contrib.auth.models import User



def registerPage(request):
    form = CreateUserForm(request.POST)
    # form2 = CreateBloggerForm(request.POST , request.FILES)

    if request.user.is_authenticated:
        return redirect('home')
        
    else:
        # form = CreateUserForm
        # form2 = CreateBloggerForm
        if request.method == "POST":
            

            if form.is_valid():

                

                user = form.save()
                username = form.cleaned_data.get('username')
                # messages.success(request, 'This is the account for' + user)
                group = Group.objects.get(name="blogger")
                user.groups.add(group)
                Blogger.objects.create(
                    user=user,
                    username = username
                    
                )
                


                return redirect('login')

            # form2.fields['username'] = "helloUSER"
            # form2.fields['user'] = User.objects.get(id = 1)
            # if form2.is_valid():
            #     print("FORM 2 is valid")
            # else:
            #     print("Nothing")
                    # picture = form2.cleaned_data.get('pic')

                    #
        

    context = {'form': form  }
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
