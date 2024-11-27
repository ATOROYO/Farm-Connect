from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import FarmerProject, InvestmentProposal, InvestmentTracking
from .forms import InvestmentProposalForm

@login_required
def investors_view(request):
    projects = FarmerProject.objects.all()
    return render(request, 'investments/investors.html', {'projects': projects})

@login_required
def submit_proposal(request, project_id):
    project = get_object_or_404(FarmerProject, id=project_id)
    if request.method == 'POST':
        form = InvestmentProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.project = project
            proposal.investor = request.user
            proposal.save()
            return redirect('investors')
    else:
        form = InvestmentProposalForm()
    return render(request, 'investments/submit_proposal.html', {'form': form, 'project': project})
