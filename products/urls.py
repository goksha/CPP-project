from django.urls import path
from . import views
urlpatterns =[
    path('', views.products, name='products'),
    path('classify/<slug:classification_slug>/',views.products, name='classification'),
    path('classify/<slug:classification_slug>/<slug:product_slug>/',views.products_details, name='products_details'),
    path('search/', views.search_products, name='search')
]