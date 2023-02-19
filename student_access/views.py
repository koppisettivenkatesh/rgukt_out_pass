from django.http import HttpRequest
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import new_out_pass , Student_images
from .form import *
import qrcode
import png
from datetime import date
import secrets
from datetime import date
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from django.urls import reverse_lazy
from django.conf import settings


def student_main(request):
        pic = Student_images.objects.all()
        return render(request,'student_main.html',{ 'images' : pic})


class student_change_password(PasswordChangeView):
        template_name = 'student_change_password.html'
        success_url = reverse_lazy('student_change_password_done_views')

class student_change_password_done(PasswordResetDoneView):
        template_name = 'confirm_success.html'

def student_approved(request):
                data = new_out_pass.objects.all()
                return render(request,'student_approved.html',{'new_request' : data})

def student_rejected(request):
        data = new_out_pass.objects.all()
        return render(request,'student_rejected.html',{'new_request' : data})

def student_pending(request):
        data = new_out_pass.objects.all()
        return render(request,'student_pending.html',{'new_request' : data} )

def student_new_out_pass(request):
        data = new_out_pass.objects.all()
        return render(request,'new_out_pass.html',{'new_request' : data} )

def student_out_pass_edit(request):
        data = new_out_pass.objects.all()
        return render(request,'student_out_pass_edit.html',{'new_request' : data} )

def outpass_delete(request):
        if request.method == 'POST':
                student_id = request.POST['student_id']
                delete = new_out_pass.objects.filter(student_id = student_id ,response= 'pending')
                delete.delete()
                return redirect('student_pending')
        else:
                return redirect('student_pending')


def outpass(request):
    if request.method == 'POST':
        first_name = request.POST ['first_name']
        last_name = request.POST['last_name']
        student_id = request.POST['student_id']
        reason = request.POST['reason']
        applied_date = request.POST['applied_date']
        out_date= request.POST['out_date']
        discription = request.POST['discription']
        if Student_images.objects.filter(student_id= student_id).exists():
                if new_out_pass.objects.filter(student_id = student_id , response = "pending" ) :
                        messages.error(request,'Already Applied  Wait For Response')
                        return redirect('student_new_out_pass')
                else:
                        out_pass_id = secrets.token_hex(32)
                        name = secrets.token_hex(20)
                        current_date = date.today()
                        date_format = current_date.strftime("%d-%m-%Y")
                        create = student_id+"-"+ date_format + "-"+ out_pass_id 
                        img = qrcode.make(create)
                        img_name = student_id +"-"+ date_format + name +".JPEG"
                        img.save(settings.MEDIA_ROOT +'/' + img_name)
                        new_out_pass.objects.create(first_name = first_name , last_name = last_name , student_id = student_id , main_reason = reason , today_date = applied_date , out_data = out_date , dis = discription , out_pass_id= create ,qr_image_name= img_name )
                        messages.success(request,"Successfuly Submited")
                        return redirect('student_new_out_pass')
        else:
                messages.error(request,'Please Upload Profile Picture')
                return redirect('student_new_out_pass')
    else:
        messages.error(request,'Something Went Wrong')
        return redirect('student_new_out_pass')

def update_out_pass(request):
    if request.method == 'POST':
        first_name = request.POST ['first_name']
        last_name = request.POST['last_name']
        student_id = request.POST['student_id']
        reason = request.POST['reason']
        applied_date = request.POST['applied_date']
        out_date= request.POST['out_date']
        discription = request.POST['discription']
        new_out_pass.objects.filter(student_id = student_id).update(first_name = first_name , last_name = last_name , student_id = student_id , main_reason = reason , today_date = applied_date , out_data = out_date , dis = discription )
        messages.success(request,"Changes are Done")
        return redirect('student_out_pass_edit')
    else:
        messages.error(request,'Something Went Wrong')
        return redirect('student_out_pass_edit')

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

def image_upload(request):
  
    if request.method == 'POST' and 'picture' in request.FILES:
        image = request.FILES
        doc_image = image['picture']
        student_id = User.objects.get(username=request.user.username)
        delete = Student_images.objects.filter(student_id=student_id)
        delete.delete()
        Student_images.objects.create(student_id=student_id,student_img = doc_image)
        messages.success(request,"Successfully Uploaded")
        return redirect(request.META['HTTP_REFERER'])  
    else:
        messages.error(request, "Something Went Wrong")
        return redirect(request.META['HTTP_REFERER'])