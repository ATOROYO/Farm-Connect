from django.urls import path
from .views import (
    browse_opportunities_view,
    submit_proposal_view,
    track_investments_view
)

urlpatterns = [
    path('investors/browse/', browse_opportunities_view, name='browse_opportunities'),
    path('investors/proposal/', submit_proposal_view, name='submit_proposal'),
    path('investors/track/', track_investments_view, name='track_investments'),
]

