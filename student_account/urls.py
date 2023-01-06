from django.urls import path
from .import views

urlpatterns = [
    path("student",views.student,name='student'),
    path("student_login",views.student_login,name='student_login'),
    path("student_sign_up",views.student_sign_up,name='student_sign_up'),
    path("signup",views.signup,name='signup'),
    path("login",views.login,name='login'),

]