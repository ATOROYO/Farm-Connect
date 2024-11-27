from django import forms
from .models import InvestmentProposal

class InvestmentProposalForm(forms.ModelForm):
    class Meta:
        model = InvestmentProposal
        fields = ['investor_name', 'email', 'proposal_amount', 'description']
