from django.db import models
from django.contrib.auth.models import User

class FarmerProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    funding_goal = models.DecimalField(max_digits=10, decimal_places=2)
    current_funding = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class InvestmentProposal(models.Model):
    project = models.ForeignKey(FarmerProject, on_delete=models.CASCADE)
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    proposal_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Proposal by {self.investor} for {self.project}"

class InvestmentTracking(models.Model):
    project = models.ForeignKey(FarmerProject, on_delete=models.CASCADE)
    investor = models.ForeignKey(User, on_delete=models.CASCADE)
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    investment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Ongoing', 'Ongoing'), ('Completed', 'Completed')])

    def __str__(self):
        return f"Tracking for {self.project} by {self.investor}"
