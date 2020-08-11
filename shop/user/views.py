from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from user.models import User
from user.forms import user_registration_form,user_info_edit
from products.models import order
# Create your views here.

def register(request):
    if request.method=='POST':
        form=user_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login/')
    else:
        form=user_registration_form()

    context={  
        "form":form
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
            return redirect('/user/login/')

    else:
        return render(request,'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('/')

def user_info(request):
    cart_items=order.objects.filter(customer=request.user).filter(status='In Cart')
    delivered_items=order.objects.filter(customer=request.user).filter(status='Delivered')
    pending_items=order.objects.filter(customer=request.user).filter(status='Pending') | order.objects.filter(customer=request.user).filter(status='Left for Delivery')
    context={
        'profile':request.user,
        'cart_items':cart_items,
        'pending_items':pending_items,
        'delivered_items':delivered_items
    }
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.POST.get('btn')=='Yes':
                delete_id=request.POST.get('delete-value')
                a=order.objects.get(id=delete_id)
                if a.status=='Left for Delivery':
                    messages.info(request,"Sorry you can't cancel a product that has left for delivery")
                else:
                    a.delete()
            elif request.POST.get('btn')=='Save Changes':
                changed_qtn= request.POST.getlist('item_qtn')
                items=cart_items
                for i in range(len(changed_qtn)):
                    item_id=items[i].id
                    a=order.objects.get(id=item_id)
                    a.quantity=changed_qtn[i]
                    a.save()
                changed_qtn=''
                items=''
                a=''
            elif request.POST.get('btn')=='Place Order':
                placed_order=request.POST.getlist('order-value')
                for order_id in placed_order:
                    a=order.objects.get(id=order_id)
                    a.status='Pending'
                    a.save()

        return render(request,'user_info.html',context)
    else:
        pass

def edituserinfo(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=user_info_edit(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                form=user_info_edit(instance=request.user)
                redirect('/user/user_info')
        else:
            form=user_info_edit(instance=request.user)

        context={
            'edit_user':request.user,
            'form':form
        }
        return render(request,'user_info_edit.html',context)
    else:
        pass

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)#important=>keeps logged in 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/user/user_info')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)

    context={
        'form':form
    }
    return render(request,'change_password.html',context)