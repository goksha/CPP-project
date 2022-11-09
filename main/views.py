from django.shortcuts import render
from products.models import Product
# Create your views here.
def homeview(request):
    products = Product.objects.all().filter(Product_isavailable=True)
    context= {
        'products':products,
    }
    return render(request,'main/index.html',context)