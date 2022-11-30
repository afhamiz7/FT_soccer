from django.urls import path
from . import views

urlpatterns=[

     path('order',views.order_page,name='order_page'),

     path('addcart',views.addcart_page,name='addcart_page'),

     path('brand',views.brand_page,name='brand_page'),

     path('buy',views.buy_page,name='buy_page'),

     path('cancel',views.cancel_page,name='cancel_page'),

     path('contact',views.contact_page,name='contact_page'),

     path('customize',views.customize_page,name='customize_page'),

     path('',views.home_page,name='home_page'),

     path('item',views.item_page,name='item_page'),

     path('payment',views.payment_page,name='payment_page'),

     path('search',views.search_page,name='search_page'),

     path('size&color',views.size_color_page,name='size_color_page'),

     path('profile',views.profile_page,name='profile_page'),
      
]