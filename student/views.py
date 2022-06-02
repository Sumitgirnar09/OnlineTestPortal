from curses.ascii import HT
from email import message
import email
from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Student
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout


# Create your views here.
def home(request):
    return render(request,'student/home.html')

def register(request):
    if request.method=="POST":
        print(request)
        f_name=request.POST.get('f_name', '')
        l_name=request.POST.get('l_name', '')
        Username=f_name+"@"+"coep"
        branch=request.POST.get('branch')
        email=request.POST.get('email', '')
        mis=request.POST.get('mis','')
        pass1=request.POST.get('pass1','')
        pass2=request.POST.get('pass2','')
        
       
        # if (pass1!= pass2):
        #      messages.error(request, " Passwords do not match")
        #      return redirect('home')
         
        # print(f_name,l_name,branch,email)
        # student = Student(f_name=f_name,l_name=l_name,branch=branch, email=email,mis=mis)
        # student.save()
        
           # Create the user
        myuser = User.objects.create_user(Username, email, pass1)
        myuser.first_name= f_name
        myuser.last_name= l_name
        myuser.branch=branch
        myuser.email=email
        myuser.mis=mis
        myuser.save()
        print("data created")
        messages.success(request, " Your  has been successfully created")
        return redirect('home')

    return render(request, "student/register.html")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            username=user.first_name+" "+ user.last_name
            login(request, user, username)
            # dict={name:user.name}
            messages.success(request, "Successfully Logged In")
            # return HttpResponse("login successful")
            return render(request,"student/afterlogin.html")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
