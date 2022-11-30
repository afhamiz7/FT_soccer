from django.shortcuts import render

# Create your views here.

def login_page(request):
    return render(request,'common/login.html')

def signup_page(request):
    return render(request,'common/signup.html')


