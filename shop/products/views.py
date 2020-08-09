from django.shortcuts import render,redirect
from products.models import product
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm


def select_six(all_products):
    result=[]
    if all_products.count()>=6:
        for i in range(6):
            result.append(all_products[i])
        return result
    else:
        return all_products

# Create your views here.
selected_six=select_six(product.objects.all())
def home(request):
    context={
        "products":selected_six
    }
    return render(request,'home.html',context)

def product(request,pk):
    context={
    }
    return render(request,'product.html',context)

def products(request):
    context={
    }
    return render(request,'products.html',context)

