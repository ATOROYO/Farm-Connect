from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('farmer/dashboard/', TemplateView.as_view(template_name="farmer_dashboard.html"), name='farmer_dashboard'),
]