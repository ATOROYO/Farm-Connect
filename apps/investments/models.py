from django.db import models
from django.contrib.auth.models import User

class FarmerProject(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="farmer_projects")
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount_required = models.DecimalField(max_digits=10, decimal_places=2)
    amount_raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_funded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class InvestmentProposal(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="investment_proposals")
    project = models.ForeignKey(FarmerProject, on_delete=models.CASCADE, related_name="proposals")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Proposal by {self.investor.username} for {self.project.title}"

class InvestmentTracking(models.Model):
    investor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="investments")
    project = models.ForeignKey(FarmerProject, on_delete=models.CASCADE, related_name="investments")
    amount_invested = models.DecimalField(max_digits=10, decimal_places=2)
    investment_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Investment by {self.investor.username} in {self.project.title}"
