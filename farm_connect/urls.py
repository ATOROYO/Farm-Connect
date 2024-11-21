from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('farmer/dashboard/', TemplateView.as_view(template_name="farmer_dashboard.html"), name='farmer_dashboard'),
    path('supplier/dashboard/', TemplateView.as_view(template_name="supplier_dashboard.html"), name='supplier_dashboard')
]