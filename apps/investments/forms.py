from django import forms
from .models import FundingProposal

class FundingProposalForm(forms.ModelForm):
    class Meta:
        model = FundingProposal
        fields = ['investor_name', 'amount', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
