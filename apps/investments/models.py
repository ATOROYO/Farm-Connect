from django.db import models

class InvestmentOpportunity(models.Model):
    farmer = models.CharField(max_length=100)
    project_name = models.CharField(max_length=150)
    description = models.TextField()
    funding_needed = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name


class FundingProposal(models.Model):
    investor_name = models.CharField(max_length=100)
    investment_opportunity = models.ForeignKey(InvestmentOpportunity, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor_name} - {self.investment_opportunity.project_name}"
