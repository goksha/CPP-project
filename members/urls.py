from django.urls import path
from .import views

urlpatterns=[
    path('register/',views.register_members, name='register'),
    path('login/',views.login_members, name='login'),
    path('logout/',views.logout_members, name='logout'),
    ]