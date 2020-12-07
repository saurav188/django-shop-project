from django.shortcuts import render,redirect
from products.models import product,order,review
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from django.core.paginator import Paginator
from products.forms import givereview

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
def home(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            product_id=request.POST['product_id']
            product_qtn=1
            addtocart(request,product_qtn,product_id)
        else:
            return redirect('/user/login')

    context={
        "products":select_six(product.objects.all())
    }
    return render(request,'home.html',context)

def product_view(request,pk):
    try:
        this_review=review.objects.filter(reviewer=request.user).get(product_id=pk)
    except:
        this_review=None
    try:
        order_placed=order.objects.filter(product_id=pk).filter(customer=request.user).filter(status='Delivered')
    except:
        order_placed=None
    if request.method=='POST':
        if request.POST.get('btn')=="Add to Cart":
            review_create_form=givereview()
            review_edit_form=givereview(instance=review)
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
        elif request.POST.get('btn')=='Post Review':
            review_create_form=givereview(request.POST)
            review_to_be_saved=review_create_form.save(commit=False)
            review_to_be_saved.product=product.objects.get(id=pk)
            review_to_be_saved.reviewer=request.user
            review_to_be_saved.save()
            review_create_form=givereview()
            review_edit_form=givereview(instance=this_review)
        elif request.POST.get('btn')=='Edit Review':
            review_create_form=givereview()
            review_edit_form=givereview(request.POST,instance=this_review)
            review_edit_form.save()
            review_edit_form= givereview(instance=this_review)
    else:
        review_create_form=givereview()
        review_edit_form=givereview(instance=this_review)
    context={
        "product":product.objects.get(id=pk),
        "givereview":review_create_form,
        "editreview":review_edit_form,
        "this_review":this_review,
        "order_placed":order_placed,
        "reviews":review.objects.filter(product_id=pk)
    }
    print(this_review)
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
    except:
        page = paginator.get_page(paginator.num_pages)
    
    context={
        'products':page,
        'num':page_number
    }
    return render(request,'products.html',context)