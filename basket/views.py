from django.shortcuts import render,redirect,get_object_or_404
from products.models import Product
from .models import Basket,Basket_item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _basket_id(request):
    basket=request.session.session_key
    if not basket:
        basket= request.session.create()
    return basket

def add_basket(request,product_id):
    product = Product.objects.get(id=product_id)
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
    basket = Basket.objects.get(basket_id=_basket_id(request))
    product= get_object_or_404(Product, id=product_id)
    basket_item = Basket_item.objects.get(product=product,basket=basket)
    if basket_item.qty > 1:
        basket_item.qty -= 1
        basket_item.save()
    else:
        basket_item.delete()
    return redirect('basket')

def remove_basket(request, product_id):
    basket = Basket.objects.get(basket_id=_basket_id(request))
    product= get_object_or_404(Product, id=product_id)
    basket_item = Basket_item.objects.get(product=product,basket=basket)
    basket_item.delete()
    return redirect('basket')    

def basket(request, total=0, qty=0, basket_item = None):
    try:
        tax=0
        grand_total=0
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


