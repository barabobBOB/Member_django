
from django.shortcuts import redirect, render
from api.forms import LoginForm, RegisterForm
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def login_view(request):
    is_ok = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = Users.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                is_ok = True
    else:
        form = LoginForm()
        
    return render(request, "login.html", {"form": form, "is_ok": is_ok})
               
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        #email, username, password
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_pass = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_pass)
            login(request, user)
            return redirect("login")
        return render(request, "login.html", {"form": form})
            
    else:
        form = RegisterForm()
    return render(request,"register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')