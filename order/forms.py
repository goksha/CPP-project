from django import forms
from .models import Order


class shippingform(forms.ModelForm):
    class Meta:
        model = Order
        fields=['first_name','last_name','email','address_line1','address_line2','eircode']
