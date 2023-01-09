from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from student_access.models import new_out_pass
from student_access.views import outpass
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from django.urls import reverse_lazy


def faculty_main(request):
        return render(request,'faculty_main.html')


def faculty_login(request):
        return render(request,'faculty_login.html')

def faculty_approved(request):
        data = new_out_pass.objects.all()
        return render(request,'faculty_approved.html',{'new_request' : data})

def faculty_rejected(request):
        data = new_out_pass.objects.all()
        return render(request,'faculty_rejected.html',{'new_request' : data})

class faculty_change_password(PasswordChangeView):
        template_name = 'faculty_change_password.html'
        success_url = reverse_lazy('faculty_change_password_done_views')

class faculty_change_password_done(PasswordResetDoneView):
        template_name = 'confirm_success.html'


def faculty_new_request(request):
        data = new_out_pass.objects.all()
        if request.method == 'POST':
                response = request.POST['response']
                student_id = request.POST['student_id']
                faculty_id = request.POST['faculty_id']
                res = response.split('-')
                if response == "pending":
                        messages.error(request,"Please Choose your Response")
                        return render(request,'faculty_new_request.html',{'new_request' : data})

                elif res[0] == 'reject':
                        new_out_pass.objects.filter(student_id = student_id,Rejected_reason = "none",response = 'pending').update(response = res[0] ,Rejected_reason = res[1] ,faculty_id = faculty_id)
                        messages.success(request,"Submitted Successfully")
                        return render(request,'faculty_new_request.html',{'new_request' : data})

                else: 
                        new_out_pass.objects.filter(student_id = student_id,Rejected_reason = "none" ,response = 'pending' ).update(response = response ,Rejected_reason = 'none' ,faculty_id = faculty_id)
                        messages.success(request,"Submitted Successfully")
                        return render(request,'faculty_new_request.html',{'new_request' : data})

        else:
                return render(request,'faculty_new_request.html',{'new_request' : data})



def logout(request):
    auth.logout(request)
    return redirect('/')


def profile_update(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user = User.objects.get(username=request.user.username)
        update = User.objects.filter(username= user).update(first_name=first_name,last_name=last_name,email = email)
        messages.success(request,"Successfully Updated")
        return redirect(request.META['HTTP_REFERER'])   

    else:
        messages.error(request, "Something Went Wrong")
        return redirect(request.META['HTTP_REFERER'])