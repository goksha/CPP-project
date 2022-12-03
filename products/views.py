from django.shortcuts import render, get_object_or_404
from .models import Product
from classifypro.models import Classifypro
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def products (request, classification_slug=None):
    classifications = None
    products = None
    if classification_slug!=None:
        classifications=get_object_or_404(Classifypro, classification_slug=classification_slug)
        products=Product.objects.filter(classification = classifications, Product_isavailable=True)
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count  = products.count()
    else:

        products = Product.objects.all().filter(Product_isavailable=True)
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context= {
        'products':paged_products,
        'count':product_count,
    }
    return render(request, 'products/products.html', context)

def products_details(request,classification_slug,product_slug):
    individual_product= Product.objects.get(classification__classification_slug=classification_slug, Product_slug=product_slug)
    context={
        'individual_product': individual_product,
    }
    return render(request,'products/products_details.html',context)

def search_products(request):
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('Product_creation').filter(Product_name__icontains=keyword)
            product_count  = products.count()
            context ={
            'products': products,
            'count': product_count,
            }
            return render(request,'products/products.html',context)
        else:
            return render(request,'products/products.html')