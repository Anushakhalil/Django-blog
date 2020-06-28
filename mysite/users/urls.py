from django.urls import path
from .views import ( registerPage,loginPage,logoutPage)

App_name= "user"

urlpatterns = [
    path("", registerPage, name="register"),
    path("login/", loginPage, name="login"),
    path("dashboard/", logoutPage, name="dashboard"),

]
