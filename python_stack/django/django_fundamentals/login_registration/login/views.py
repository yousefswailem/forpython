from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
from .models import Users
# Create your views 

def index(request):
    return render(request,"index.html")

def login(request,email):
    if request.method =="POST" :
        if request.POST["login_type"] =="login":
            if models.check_user(request.POST["email"],request.POST["password"]):
                return render(request, "welcome.html")
            
        if request.POST["login_type"] =="login_registration":
            models.register(request.POST["email"],request.POST["name"],request.POST["password"])

        errors = Users.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        elif  request.method == 'POST' :
            error = Users.objects.get (email=email)
            error.name = request.POST['name']
            error.password = request.POST['password']
            messages.success(request, "user successfully updated")
            error.save()
            return redirect('/login')