from django.urls import path
from .import views

urlpatterns = [
    path("faculty",views.faculty,name='faculty'),
    path("faculty_login",views.faculty_login,name='faculty_login'),
    path("faculty_sign_up",views.faculty_sign_up,name='faculty_sign_up'),
    path("signup",views.signup,name='signup'),
    path("login",views.login,name='login'),


]