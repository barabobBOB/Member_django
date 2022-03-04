from django.shortcuts import redirect, render
from api.forms import LoginForm, RegisterForm
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    is_ok = False
    user = None
    msg = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            try:
                user = Users.objects.get(username=username)
                msg = "올바른 유저네임과 패스워드를 입력해주세요."
            except Users.DoesNotExist:
                pass
            else:
                if user.check_password(password):
                    login(request, user)
                    is_ok = True       
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form, "is_ok": is_ok, "msg": msg})
               
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
        return render(request, "register.html", {"form": form})
            
    else:
        form = RegisterForm()
    return render(request,"register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def userlist_view(request,userid):
    if request.method == "GET":
        #첫페이지
        page = request.GET.get("page", 1)
        #아이디 값을 기준으로 유저정보 가져옴
        users = Users.objects.all().order_by("id")
        #페이지 단위로 쪼개????????/////////
        paginator = Paginator(users, 10)
        page_object = paginator.get_page(page)
        
        return render(request, "userlist.html", {"page_object":page_object})        