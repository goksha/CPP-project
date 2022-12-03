from django.db import models
from products.models import Product
# Create your models here.
class Basket(models.Model):
    basket_id=models.CharField(max_length=250, blank=True)
    basket_date_add=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.basket_id

class Basket_item(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    basket= models.ForeignKey(Basket, on_delete=models.CASCADE)
    qty=models.IntegerField()
    is_active=models.BooleanField(default=True)

    def totalval(self):
        return self.product.Product_price * self.qty

    def __str__(self):
        return self.product