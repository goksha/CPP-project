from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_name','Product_isavailable', 'Product_price','Product_stock','Product_modification')
    prepopulated_fields= {'Product_slug':('Product_name',)}


admin.site.register(Product,ProductAdmin)
