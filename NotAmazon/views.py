from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from .models import Item

# Creating a register form class
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields= ["username", "email", "password", "password2"]

# Create your views here.
def index(request):
    context = {}
    context["Title"] = "test"
    return render(request, "home.html", context)

def products(request):
    return render(request, "products.html", {})

def shop(request):
    # Create a list of items in the Item table
    item_list = Item.objects.all()

    # Item dictionary
    context = {"item_list":item_list}
    return render(request, "shop.html", context)



def user_login(request):
    form = AuthenticationForm(request.POST)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "registration/user_login.html", {"form":form})

def user_signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    
    else:
        form = RegistrationForm()
    return render(request, "registration/user_signup.html", {"form":form})