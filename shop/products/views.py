from django.shortcuts import render,redirect
""" from products.models import produuct,banner,description_pics,userprofile,order,review """
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm

# Create your views here.
def home(request):
    context={
    }
    return render(request,'home.html',context)

def product(request,pk):
    context={
    }
    return render(request,'product.html',context)

def products(request,page_no):
    context={
    }
    return render(request,'products.html',context)

