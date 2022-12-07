from django.shortcuts import render,redirect
from basket.models import Basket,Basket_item
from .forms import shippingform
from .models import Order,Payment,OrderProduct
from products.models import Product 
import datetime
# Create your views here.
def placeorder(request, total=0, qty=0):
    current_user=request.user

    basket_items= Basket_item.objects.filter(user=current_user)
    count=basket_items.count()
    if count <= 0:
        return redirect('products')
    
    grand_total=0
    tax=0
    for item in basket_items:
        total += (item.product.Product_price * item.qty)
        qty +=  item.qty
    tax = (5*total)/100
    grand_total = total+tax        
    
    if request.method == 'POST':
        form=shippingform(request.POST)
        if form.is_valid():
            shipping_data = Order()
            shipping_data.user= current_user
            shipping_data.first_name = form.cleaned_data['first_name']
            shipping_data.last_name = form.cleaned_data['last_name']
            shipping_data.email = form.cleaned_data['email']
            shipping_data.address_line1 = form.cleaned_data['address_line1']
            shipping_data.address_line2 = form.cleaned_data['address_line2']
            shipping_data.eircode = form.cleaned_data['eircode']
            shipping_data.order_total = grand_total
            shipping_data.tax = tax
            shipping_data.save()

            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")
            order_number=current_date+str(shipping_data.id)
            shipping_data.order_number=order_number
            shipping_data.save()

            order=Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order': order,
                'basket_item': basket_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
            }            
            return render(request,'order/payments.html',context)
    else:        
        return redirect('checkout')


def payments(request):
    return render(request,'order/payments.html')