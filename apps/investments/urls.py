from django.urls import path
from .views import investors_view, submit_proposal

urlpatterns = [
    path('investors/', investors_view, name='investors'),
    path('submit-proposal/<int:project_id>/', submit_proposal, name='submit_proposal'),
]
