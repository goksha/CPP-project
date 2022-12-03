from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.
def register_members(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("Sign Up was successfull"))
            return redirect ('home')
    else:
        form = CreateUserForm()
    context={
        'form':form,
    }
    return render(request,'members/register.html',context)

def login_members(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')
        else:
            messages.info(request,("Username or Password Incorrect"))
            return redirect('login')
    else:
        return render(request,'members/login.html')

def logout_members(request):
    logout(request)
    return redirect('home')