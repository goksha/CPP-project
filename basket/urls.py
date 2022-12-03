from django.urls import path
from . import views


urlpatterns=[
    path('',views.basket,name='basket'),
    path('add_basket/<int:product_id>/',views.add_basket, name='add_basket'),
    path('sub_basket/<int:product_id>/',views.sub_basket, name='sub_basket'),
    path('remove_basket/<int:product_id>/',views.remove_basket, name='remove_basket'),
]