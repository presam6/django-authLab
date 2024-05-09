from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# - Homepage
def homepage(request):
    return render(request, 'myapp/homepage/index.html')

# - Register Page
def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect("login")
        
    context = {'registerform': form}
        
    return render(request, 'myapp/register/register.html', context = context)

# - Login Page
def user_login (request):
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data = request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password )
            if user is not None:
                auth.login(request, user)
                
                return redirect("dashboard")
            
    context = {'loginform': form}
    return render(request, 'myapp/user-login/login.html', context = context)

# - Logout Func
def user_logout(request):
    
    auth.logout(request)
    
    return redirect ("")

# - Login Required Decorator 
@login_required(login_url="login")


# - Dashboard Page
def dashboard (request):
    return render(request, 'myapp/dashboard/dashb.html')

