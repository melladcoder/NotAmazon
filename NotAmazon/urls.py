from django.urls import path 

from . import views 

# direct list 
urlpatterns = [
    path("home", views.index, name="home"),
    path("products", views.products, name="products"),
    path("shop", views.shop, name="shop"),
    path("signup", views.user_signup, name="user_signup"),
    path("login", views.user_login, name="user_login"),
    
]