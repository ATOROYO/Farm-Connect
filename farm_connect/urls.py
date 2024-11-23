from django.contrib import admin
from django.urls import path
from apps.marketplace.views import about_view
from apps.marketplace.views import farmer_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_view, name='about'),
    path('marketplace/farmer/dashboard/', farmer_dashboard, name='farmer_dashboard'),
    path('supplier/dashboard/', about_view, name='supplier_dashboard')
]