from django.shortcuts import render, get_object_or_404, redirect
from .models import InvestmentOpportunity, FundingProposal
from .forms import FundingProposalForm


def browse_opportunities(request):
    opportunities = InvestmentOpportunity.objects.all()
    return render(request, 'investments/browse.html', {'opportunities': opportunities})


def submit_proposal(request, opportunity_id):
    opportunity = get_object_or_404(InvestmentOpportunity, id=opportunity_id)
    if request.method == 'POST':
        form = FundingProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.investment_opportunity = opportunity
            proposal.save()
            return redirect('track_investments')
    else:
        form = FundingProposalForm()
    return render(request, 'investments/submit_proposal.html', {'form': form, 'opportunity': opportunity})


def track_investments(request):
    proposals = FundingProposal.objects.all()
    return render(request, 'investments/track.html', {'proposals': proposals})
