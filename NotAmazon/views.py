from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

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


def signup(request):
    return render(request, "signup.html", {})
    
def thankyou(request):
    return render(request, "thankyou.html", {})
        
def login(request):
    return render(request, "login.html", {})
