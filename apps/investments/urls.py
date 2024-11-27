from django.urls import path
from . import views

urlpatterns = [
    path('', views.investors_view, name='investors'),  
    path('investors/', views.investors_view, name='investors'),
    path('submit-proposal/<int:project_id>/', views.submit_proposal, name='submit_proposal'),
]

