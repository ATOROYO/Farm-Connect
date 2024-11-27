from django.db import models

class InvestmentProposal(models.Model):
    investor_name = models.CharField(max_length=100)
    email = models.EmailField()
    proposal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.investor_name} - {self.proposal_amount}"
