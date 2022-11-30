from django.urls import path
from . import views
urlpatterns =[
    path('', views.products, name='products'),
    path('<slug:classification_slug>/',views.products, name='classification'),
    path('<slug:classification_slug>/<slug:product_slug>/',views.products_details, name='products_details'),
]