from django.urls import path
from . import views

urlpatterns = [
    path('', views.investment_list, name='investment_list'),  # List of investments
    path('submit/', views.submit_proposal, name='submit_proposal'),  # Submit proposal
    path('<int:pk>/', views.investment_detail, name='investment_detail'),  # Investment detail
]


