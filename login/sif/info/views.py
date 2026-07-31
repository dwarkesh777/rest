# pyrefly: ignore [missing-import]
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout
from .models import sif
# Create your views here.

def home(request):
    data = sif.objects.all()
    return render(request, 'home.html', {'data': data})

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect("login")

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        enrollment = request.POST.get('enrollment')
        roll = request.POST.get('roll')
        dob = request.POST.get('dob')
        title = request.POST.get('title')
        sif.objects.create(name=name, enrollment=enrollment, roll=roll, dob=dob, title=title)
        return redirect('home')

    return render(request, 'form.html')

def update(request, id):

    d = get_object_or_404(sif,
        id=id
    )

    if request.method == 'POST':

        d.name = request.POST.get('name')
        d.enrollment = request.POST.get('enrollment')
        d.roll = request.POST.get('roll')
        d.dob = request.POST.get('dob')
        d.title = request.POST.get('title')

        d.save()

        return redirect('home')

    return render(
        request,
        'update.html',
        {'data': d}
    )

def delete(req,id):
    d=get_object_or_404(sif,id=id)
    d.delete()
    return redirect("home")


