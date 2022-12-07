from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from .models import Basket,Basket_item
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.

def _basket_id(request):
    basket=request.session.session_key
    if not basket:
        basket= request.session.create()
    return basket

def add_basket(request,product_id):
    current_user=request.user
    product = Product.objects.get(id=product_id)
    #user authenticated
    if current_user.is_authenticated:
        try:
            basket_item=Basket_item.objects.get(product=product,user=current_user)
            basket_item.qty +=1
            basket_item.save()
        except Basket_item.DoesNotExist:
            basket_item=Basket_item.objects.create(
                product = product,
                qty = 1,
                user = current_user,
            )
            basket_item.save()
        return redirect('basket')
    #if user is not authenticated
    else:
        try:
            basket = Basket.objects.get(basket_id=_basket_id(request))
        except Basket.DoesNotExist:
            basket=Basket.objects.create(
                basket_id=_basket_id(request)
            )
        basket.save()

        try:
            basket_item=Basket_item.objects.get(product=product,basket=basket)
            basket_item.qty +=1
            basket_item.save()
        except Basket_item.DoesNotExist:
            basket_item=Basket_item.objects.create(
                product = product,
                qty = 1,
                basket = basket,
            )
            basket_item.save()
        return redirect('basket')

def sub_basket(request, product_id):
    current_user=request.user
    
    product= get_object_or_404(Product, id=product_id)
    try:
        if current_user.is_authenticated:
            basket_item = Basket_item.objects.get(product=product,user=current_user)
        else:
            basket = Basket.objects.get(basket_id=_basket_id(request))
            basket_item = Basket_item.objects.get(product=product,basket=basket)
        if basket_item.qty > 1:
            basket_item.qty -= 1
            basket_item.save()
        else:
            basket_item.delete()
    except:
        pass
    return redirect('basket')

def remove_basket(request, product_id):
    
    product= get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        basket_item = Basket_item.objects.filter(product=product,user=request.user)

    else:
        basket = Basket.objects.get(basket_id=_basket_id(request))
        basket_item = Basket_item.objects.get(product=product,basket=basket)
    basket_item.delete()
    return redirect('basket')    

def basket(request, total=0, qty=0, basket_item = None):
    try:
        tax=0
        grand_total=0
        if request.user.is_authenticated:
            basket_item=Basket_item.objects.filter(user=request.user, is_active=True)
        else:    
            basket= Basket.objects.get(basket_id=_basket_id(request))
            basket_item=Basket_item.objects.filter(basket=basket, is_active=True)
        for item in basket_item:
            total += (item.product.Product_price * item.qty)
            qty +=  item.qty
        tax = (5*total)/100
        grand_total = total+tax    
    except ObjectDoesNotExist:
        pass

    context ={
        'total':total,
        'qty':qty,
        'basket_item':basket_item,
        'tax':tax,
        'grand_total':grand_total,

    }
    return render(request,'basket/basket.html',context)

@login_required(login_url='login')
def checkout(request,total=0, qty=0, basket_item = None):
    try:
        tax=0
        grand_total=0
        if request.user.is_authenticated:
            basket_item=Basket_item.objects.filter(user=request.user, is_active=True)
        else:    
            basket= Basket.objects.get(basket_id=_basket_id(request))
            basket_item=Basket_item.objects.filter(basket=basket, is_active=True)
        for item in basket_item:
            total += (item.product.Product_price * item.qty)
            qty +=  item.qty
        tax = (5*total)/100
        grand_total = total+tax    
    except ObjectDoesNotExist:
        pass

    context ={
        'total':total,
        'qty':qty,
        'basket_item':basket_item,
        'tax':tax,
        'grand_total':grand_total,

    }    
    return render(request,'basket/checkout.html',context)