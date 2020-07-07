from django.shortcuts import render
from django.http import HttpResponse
def site(request):
    return render(request,'flybuy.html')
def hello(request):
    return HttpResponse("Hello Hemant is here")
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def city(request):
    return render(request,'city.html')
def cart(request):
    return render(request,'cart.html')
def fruits(request):
    return render(request,'fruits.html')
def personalcare(request):
    return render(request,'personalcare.html')
def cleanising(request):
    return render(request,'cleanising.html')