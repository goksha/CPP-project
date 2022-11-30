from django.db import models

# Create your models here.
class Classifypro (models.Model):
    classification_name= models.CharField(max_length=70, unique=True)
    slug= models.CharField(max_length=100, unique=True)
    description= models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.classification_name