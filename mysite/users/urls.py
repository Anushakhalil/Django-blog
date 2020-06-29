from django.urls import path
from .views import ( registerPage,loginPage )

App_name= "user"

urlpatterns = [
    path("signup/", registerPage, name="register"),
    path("login/", loginPage, name="login"),
    #path("dashboard/", logoutPage, name="dashboard"),

]
