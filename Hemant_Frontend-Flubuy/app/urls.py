from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.hello),
    path('site',views.site),
    path('login',views.login),
    path('signup',views.signup),
    path('city',views.city),
    path('cart',views.cart),
    path('fruits',views.fruits),
    path('personalcare',views.personalcare),
    path('cleanising',views.cleanising),
]
