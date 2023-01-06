from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def student(request):
    return render(request,'student.html')


def student_login(request):
    return render(request,'student_login.html')

def student_sign_up(request):
    return render(request,'student_sign_up.html')


def login(request):

    if request.method == 'POST':
        student_id = request.POST['student_id']
        passwd = request.POST['password']
        for check in  student_id:
            if check == "r":
                user = authenticate(username =  student_id , password = passwd)
                if user is not None:
                    auth.login(request,user)
                    return redirect('student_main')
                else:
                    messages.error(request,'ID or Password are Invalid')
                    return redirect('student_login')
            elif check == "R":
                user = authenticate(username =  student_id , password = passwd)
                if user is not None:
                    auth.login(request,user)
                    return redirect('student_main')
                else:
                    messages.error(request,'ID or Password are Invalid')
                    return redirect('student_login')
            elif check == "f":
                messages.error(request,'Please Login with Student credentials')
                return redirect('student_login')
            elif check == "F":
                messages.error(request,'Please Login with Student credentials')
                return redirect('student_login')
            else:
                messages.error(request,'Please Login with Student credentials')
                return redirect('student_login')
    else:
        messages.error(request,'Something Went Wrong')
        return redirect('student_login')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST ['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        student_id = request.POST['student_id']
        passwd_1 = request.POST['passwd_1']
        confirm= request.POST['confirm']
        if passwd_1 == confirm:
            if User.objects.filter(username = student_id).exists():
                messages.error(request,"Student ID Exists")
                return redirect('student_sign_up')
            elif User.objects.filter(email = email).exists():
                messages.error(request,"Email Already Exists")
                return redirect('student_sign_up')

            else:
                user = User.objects.create_user(username = student_id , email = email, password = passwd_1 ,first_name = first_name , last_name = last_name)
                user.save();
                messages.success(request,"SignUp Is Successful")
                return redirect('student_sign_up')
        else:
            messages.error(request,"Password Not Matched")
            return redirect('student_sign_up')
    else:
        messages.error(request,'Something Went Wrong')
        return redirect('student_sign_up')
 
def logout(request):
    auth.logout(request)
    return redirect('/')
