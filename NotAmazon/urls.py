from django.urls import path 

from . import views 

# direct list 
urlpatterns = [
    path("home", views.index, name="index"),
    path("products", views.products, name="products"),
    path("shop", views.shop, name="shop"),
    path("signup", views.signup, name="signup"),
    path("thankyou", views.thankyou, name="thankyou"),
    path("login", views.login, name="login"),
]