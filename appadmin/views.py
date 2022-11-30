from django.shortcuts import render
 
# Create your views here.


def user_details(request):
    return render(request,'appadmin/userdetails.html')

def profile_update(request):
    return render(request,'appadmin/profileupdate.html')

def stock_update(request):
    return render(request,'appadmin/stockupdate.html')

def payment_details(request):
    return render(request,'appadmin/paymentdetails.html')   

def home(request):
    return render(request,'appadmin/admin_home.html')   
    
