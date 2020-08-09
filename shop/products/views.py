from django.shortcuts import render,redirect
from products.models import product
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from django.core.paginator import Paginator

all_product= product.objects.all()
def select_six(all_products):
    result=[]
    if all_products.count()>=6:
        for i in range(6):
            result.append(all_products[i])
        return result
    else:
        return all_products

# Create your views here.
selected_six=select_six(all_product)
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
    paginator = Paginator(all_product, 12)
    try:
        page_number = int(request.GET.get('page'))
    except:
        page_number=1
    try:
        page = paginator.get_page(page_number)
    except(EmptyPage, InvalidPage):
        page = paginator.get_page(paginator.num_pages)
    
    context={
        'products':page,
        'num':page_number
    }
    return render(request,'products.html',context)

