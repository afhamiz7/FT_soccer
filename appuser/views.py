from django.shortcuts import render

# Create your views here.


def order_page(request):
    return render(request,'appuser/order.html')

def addcart_page(request):
    return render(request,'appuser/addcart.html')

def brand_page(request):
    return render(request,'appuser/brand.html')

def buy_page(request):
    return render(request,'appuser/buy.html')

def cancel_page(request):
    return render(request,'appuser/canceloption.html')

def contact_page(request):
    return render(request,'appuser/contact.html')

def customize_page(request):
    return render(request,'appuser/customize.html')

def home_page(request):
    return render(request,'appuser/homepage.html')

def item_page(request):
    return render(request,'appuser/item.html')

def payment_page(request):
    return render(request,'appuser/payment.html')

def search_page(request):
    return render(request,'appuser/search.html')

def size_color_page(request):
    return render(request,'appuser/size&color.html')

def profile_page(request):
    return render(request,'appuser/profile.html')    
    



    
    



