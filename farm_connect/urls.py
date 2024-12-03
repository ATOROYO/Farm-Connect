from django.contrib import admin
from django.urls import path
from django.urls import include, path
from apps.marketplace.views import about_view
from apps.marketplace.views import contact_view
from apps.marketplace.views import farmer_dashboard
from apps.marketplace.views import supplier_dashboard
from apps.buyers.views import buyer_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('marketplace/farmer/dashboard/', farmer_dashboard, name='farmer_dashboard'),
    path('marketplace/supplier/dashboard/', supplier_dashboard, name='supplier_dashboard'),
    path('investments/', include('apps.investments.urls')),
    path('buyers/', include('apps.buyers.urls')),
]
