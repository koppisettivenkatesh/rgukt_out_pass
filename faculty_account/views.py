from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages





def faculty(request):
    return render(request,'faculty.html')

def faculty_login(request):
    return render(request,'faculty_login.html')

def faculty_sign_up(request):
    return render(request,'faculty_sign_up.html')


def login(request):
    
    if request.method == 'POST':
        faculty_id = request.POST['faculty_id']
        passwd = request.POST['password']
        for check in faculty_id:
            if check == "f":
                user = authenticate(username = faculty_id , password = passwd)
                if user is not None:
                    auth.login(request,user)
                    return redirect('faculty_main')
                else:
                    messages.error(request,'ID or Password are Invalid')
                    return redirect('faculty_login')
            elif check == "F":
                user = authenticate(username = faculty_id , password = passwd)
                if user is not None:
                    auth.login(request,user)
                    return redirect('faculty_main')
                else:
                    messages.error(request,'ID or Password are Invalid')
                    return redirect('faculty_login')
            elif check == "r":
                messages.error(request,'Please Login with Faculty credentials')
                return redirect('faculty_login')
            elif check == "R":
                messages.error(request,'Please Login with Faculty credentials ')
                return redirect('faculty_login')
            else:
                break
    else:
        messages.error(request,'Something Went Wrong')
        return redirect('faculty_login')



def signup(request):
    if request.method == 'POST':
        first_name = request.POST ['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        faculty_id = request.POST['faculty_id']
        passwd_1 = request.POST['passwd_1']
        confirm= request.POST['confirm']
        if passwd_1 == confirm:
            if User.objects.filter(username = faculty_id).exists():
                messages.error(request,"Faculty ID Exists")
                return redirect('faculty_sign_up')

            elif User.objects.filter(email = email).exists():   
                messages.error(request,"Email Already Exists")
                return redirect('faculty_sign_up')

            else:
                user = User.objects.create_user(username = faculty_id , email = email, password = passwd_1 ,first_name = first_name , last_name = last_name)
                user.save();
                messages.success(request,"SignUp Is Successful")
                return redirect('faculty_sign_up')
        else:   
            messages.error(request,"Password Not Matched")
            return redirect('faculty_sign_up')
    else:
        messages.error(request,'Something Went Wrong')
        return redirect('faculty_sign_up')

