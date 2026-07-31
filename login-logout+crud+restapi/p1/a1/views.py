from django.shortcuts import render,redirect,get_object_or_404
# pyrefly: ignore [missing-import]
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
from .models import std
from .serializers import seristd

# pyrefly: ignore [missing-import]
from rest_framework import viewsets

class seri(viewsets.ModelViewSet):
    queryset=std.objects.all()
    serializer_class=seristd
    

def home(reqest):
    data=std.objects.all()
    return render (reqest,"home.html",{"data":data})

    
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("home")

    else :
        form=AuthenticationForm()


    return render(request,"login.html",{"form":form})

    
def logout_view(request):
    logout(request)
    return redirect("login")

def form1(request):
    if request.method == "POST":
        name=request.POST.get("name")
        age=request.POST.get("age")
        std.objects.create(name=name,age=age)
        return redirect("home")
    
    return render(request,"form1.html")


def delete(request,id):
    d=get_object_or_404(std,id=id)
    d.delete()
    return redirect("home")

def edit(request,id):
    d=get_object_or_404(std,id=id)

    if request.method == "POST":
        d.name=request.POST.get("name")
        d.age=request.POST.get("age")
        d.save()
        return redirect("home")
    return render(request,"update.html" , {"data":d})
