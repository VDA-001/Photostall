from django.shortcuts import render, redirect
from stall.models import *
from django.contrib.auth.forms import UserCreationForm
from stall.forms import ImageForm
from django import template
from django.contrib import messages

# Create your views here.
def index(request):
    images=Image.objects.all()
    data={'images':images}
    return render(request, 'index.html',data)
def Topic(request):
    cats=Category.objects.all()
    data1={'cats':cats}
    return render(request,'Topic.html',data1)
def Images(request,cid):
    cats=Category.objects.all()
    cat=Category.objects.get(pk=cid)
    images=Image.objects.filter(category=cat)
    data3={'images':images,'cat':cat}
    return render(request,'Images.html',data3)
def Submit(request):
    if request.user.is_authenticated:
        context={}
        context['form']=ImageForm()
        if request.method == 'POST':
            form=ImageForm(request.POST,request.FILES)
            if form.is_valid():
                instance=form.save(commit=False)
                instance.username_id= request.user.pk
                print(request.user)
                instance.save()
                messages.info(request,'Success')
                return redirect('/')
            else:
                messages.info(request,'Nope')
                return redirect('Submit/')
        else:
            return render(request,"Submit.html",context)
    else:
        messages.info(request,'Login to submit a photo')
        return redirect('/accounts/Login')
register=template.Library()
@register.simple_tag
def get_username_from_userid(username):
    try:
        return User.objects.get(id=username).username
    except User.DowsNotExist:
        return 'Unknown'
def Profile(request,Uid):
    user1=User.objects.all()
    user2=User.objects.get(username=Uid)
    images=Image.objects.filter(username_id=user2)
    data4={'user2':user2,'images':images}
    return render(request,'Profile.html',data4)