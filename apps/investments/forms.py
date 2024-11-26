from django import forms
from .models import InvestmentProposal

class ProposalForm(forms.ModelForm):
    class Meta:
        model = InvestmentProposal
        fields = ['amount', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
