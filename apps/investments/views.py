from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .forms import InvestmentProposalForm
from .models import InvestmentProposal

def submit_proposal(request):
    if request.method == 'POST':
        form = InvestmentProposalForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form to the database
            return render(request, 'investments/thank_you.html')
    else:
        form = InvestmentProposalForm()

    return render(request, 'investments/submit_proposal.html', {'form': form})

def investment_list(request):
    investments = InvestmentProposal.objects.all()
    return render(request, 'investments/investment_list.html', {'investments': investments})

def investment_detail(request, pk):
    investment = get_object_or_404(InvestmentProposal, pk=pk)
    return render(request, 'investments/investment_detail.html', {'investment': investment})
