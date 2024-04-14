from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path("",views.index,name="home"),
    path("home",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("user",views.user,name="user"),
    path("afilter",views.afilter,name="afilter"),
    path("result",views.result,name="result"),

]
