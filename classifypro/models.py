from django.db import models
from django.urls import reverse
# Create your models here.
class Classifypro (models.Model):
    classification_name= models.CharField(max_length=70, unique=True)
    classification_slug= models.SlugField(max_length=100, unique=True)
    description= models.TextField(max_length=255, blank=True)

    def get_url(self):
        return reverse('classification', args=[self.classification_slug])

    def __str__(self):
        return self.classification_name