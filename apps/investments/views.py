from django.shortcuts import render, redirect
from .models import FarmerProject, InvestmentProposal, InvestmentTracking
from django.contrib.auth.decorators import login_required
from .forms import ProposalForm

@login_required
def investors_view(request):
    projects = FarmerProject.objects.filter(is_funded=False)
    investments = InvestmentTracking.objects.filter(investor=request.user)
    context = {
        'projects': projects,
        'investments': investments,
    }
    return render(request, 'investments/investors.html', context)

@login_required
def submit_proposal(request, project_id):
    project = FarmerProject.objects.get(id=project_id)
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.investor = request.user
            proposal.project = project
            proposal.save()
            return redirect('investors')
    else:
        form = ProposalForm()
    return render(request, 'investments/proposal_form.html', {'form': form, 'project': project})
