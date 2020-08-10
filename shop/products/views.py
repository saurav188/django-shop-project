from django.shortcuts import render,redirect
from products.models import product,order
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

def addtocart(request,product_qtn,product_id):
    user=request.user
    item=order(customer=user,product=product.objects.get(id=product_id),status='In Cart',quantity=product_qtn)
    item.save()
# Create your views here.
selected_six=select_six(all_product)
def home(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            product_id=request.POST['product_id']
            product_qtn=1
            addtocart(request,product_qtn,product_id)
        else:
            return redirect('/user/login')

    context={
        "products":selected_six
    }
    return render(request,'home.html',context)

def product_view(request,pk):
    if request.method=='POST':
        if request.user.is_authenticated:
            product_id=pk
            product_qtn=request.POST.get('quantity-product')
            if product_qtn!="":
                if int(product_qtn)>0: 
                    addtocart(request,product_qtn,product_id)
                else:
                    messages.info(request,'Please add quantity.')
            else:
                messages.info(request,'Please add quantity.')
        else:
            return redirect('/user/login')
    context={
        "product":product.objects.get(id=pk)
    }
    return render(request,'product.html',context)

def products(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            product_id=request.POST['product_id']
            product_qtn=1
            addtocart(request,product_qtn,product_id)
        else:
            return redirect('/user/login')

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

