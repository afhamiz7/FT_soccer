from django.urls import path
from . import views

urlpatterns=[

    path('user_details',views.user_details,name='user_page'),

    path('profile_update',views.profile_update,name='profile_page'),

    path('stock_update',views.stock_update,name='stock_page'),

    path('payment_details',views.payment_details,name='payment_page'),

    path('admin_home',views.home,name='home'),
] 
      
 
    
      


  
