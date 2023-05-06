from django.urls import path
from . import views


urlpatterns = [

    path('', views.index),
    path('control', views.control),
    path('register/student', views.register),
    path('logout', views.logout),
    path('homepage', views.homepage),
    path('login', views.login),
]