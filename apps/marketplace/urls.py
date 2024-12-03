from django.urls import path  
from .views import (  
    homepage,   
    about_page,  
    contact_page,  
    suppliers_dashboard,  
    farmers_dashboard,  
    marketplace_product_list,  # Import your new view   
)  

urlpatterns = [  
    path('', homepage, name='homepage'),  # Assuming you have a homepage view  
    path('about/', about_page, name='about'),  
    path('contact/', contact_page, name='contact'),  
    path('suppliers/dashboard/', suppliers_dashboard, name='suppliers_dashboard'),  
    path('farmers/dashboard/', farmers_dashboard, name='farmers_dashboard'),   
    path('marketplace/', marketplace_product_list, name='marketplace_product_list'),  # New URL for the marketplace  
]
