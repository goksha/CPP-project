from django.contrib import admin
from .models import Classifypro
# Register your models here.

class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('classification_name',)
    prepopulated_fields= {'classification_slug':('classification_name',)}

admin.site.register(Classifypro,ClassifyAdmin)