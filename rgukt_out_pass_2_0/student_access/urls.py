from django.urls import path
from .import views
from .views import student_change_password , student_change_password_done

urlpatterns = [
    path("student_main",views.student_main,name='student_main'),
    path("logout",views.logout,name='logout'),
    path("outpass",views.outpass,name='outpass'),
    path("student_approved",views.student_approved,name='student_approved'),
    path("student_pending",views.student_pending,name='student_pending'),
    path("student_rejected",views.student_rejected,name='student_rejected'),
    path("student_new_out_pass",views.student_new_out_pass,name='student_new_out_pass'),
    path("student_out_pass_edit",views.student_out_pass_edit,name='student_out_pass_edit'),
    path("update_out_pass",views.update_out_pass,name='update_out_pass'),
    path("student_change_password/",student_change_password.as_view(),name='student_change_password_views'),
    path('student_change_password/done/',student_change_password_done.as_view(),name='student_change_password_done_views'),
    path('outpass_delete',views.outpass_delete,name='outpass_delete'),
    path('profile_update',views.profile_update,name="profile_update"),
    path('image_upload',views.image_upload,name="image_upload"),
]