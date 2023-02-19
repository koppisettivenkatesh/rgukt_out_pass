from django.urls import path
from .import views

from .views import faculty_change_password , faculty_change_password_done


urlpatterns = [
    path("faculty_main",views.faculty_main,name='faculty_main'),
    path("faculty_approved",views.faculty_approved,name='faculty_approved'),
    path("faculty_rejected",views.faculty_rejected,name='faculty_rejected'),
    path("faculty_new_request",views.faculty_new_request,name='faculty_new_request'),
    path("logout",views.logout,name='logout'),
    path("faculty_change_password/",faculty_change_password.as_view(),name='faculty_change_password_views'),
    path('faculty_change_password/done/',faculty_change_password_done.as_view(),name='faculty_change_password_done_views'),
    path('profile_update',views.profile_update,name="profile_update"),


]