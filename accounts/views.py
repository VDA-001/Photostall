from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
def Register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('Register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                messages.info(request,'Success')
                return redirect('Login')
        else:
            messages.info(request,'Password does not match')
            return redirect('Register')
    return render(request,'Register.html')
def Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('Login')
    else:
        return render(request,"Login.html")
def Logout(request):
    auth.logout(request)
    return redirect('/')

