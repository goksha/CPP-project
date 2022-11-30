from django.db import models
from classifypro.models import Classifypro
# Create your models here.
class Product(models.Model):
    Product_name=models.CharField(max_length=200, unique=True)
    Product_price=models.FloatField()
    Product_discription=models.TextField(max_length=200, blank=True)
    Product_stock=models.IntegerField()
    Product_isavailable=models.BooleanField(default=True)
    Product_creation=models.DateTimeField(auto_now_add=True)
    Product_modification=models.DateTimeField(auto_now=True)
    Product_slug=models.SlugField(max_length=200, unique=True)
    Product_img=models.ImageField(upload_to='media/product_photos')
    classification=models.ForeignKey(Classifypro, on_delete=models.CASCADE)

    def __str__(self):
        return self.Product_name
