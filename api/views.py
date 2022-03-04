
from django.shortcuts import redirect, render
from api.forms import LoginForm, RegisterForm
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def login_view(request):
    msg = None
    is_ok = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            msg = "올바른 이메일과 패스워드를 입력하시오"
            user = Users.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                is_ok = True
                msg = None
    else:
        form = LoginForm()
        
    return render(request, "login.html", {"form": form, "msg": msg, "is_ok": is_ok})
               
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