from django.shortcuts import render,redirect
from user.models import User
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm,UserCreationForm
from django.core.paginator import Paginator

# Create your views here.

def register(request):
    if request.method=='POST':
        pass
    else:
        context={  
        } 
        return render(request,'register.html',context)

def login(request):
    context={
    }
    if request.method=='POST':
        User_name=request.POST['user_name']
        password=request.POST['password']

        user=auth.authenticate(username=User_name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Wrong info.Try again")
            return redirect('/login/')

    else:
        return render(request,'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('/')

def user_info(request):
    context={
        'profile':request.user,
    }
    if request.user.is_authenticated:
        return render(request,'user_info.html',context)
    else:
        pass

def edituserinfo(request):
    context={
        'edit_user':request.user
    }
    if request.user.is_authenticated:
        return render(request,'user_info_edit.html',context)
    else:
        pass

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/user')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)

    context={
        'form':form
    }
    return render(request,'change_password.html',context)