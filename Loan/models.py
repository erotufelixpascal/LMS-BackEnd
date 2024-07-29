import uuid
from django.db import IntegrityError, models
import Loan
from Manager.models import Users, loanCategorys
from django.db.models.signals import post_save
from django.dispatch import receiver

# default_customer = Users.objects.first()  ,default=default_customer- '18c8ca88c8834e4e921d007110232d74'

# Create your models here.
class LoanApplication(models.Model):
    customerID = models.ForeignKey(Users, on_delete = models.CASCADE, related_name='loan_user' )
    totalAmount = models.IntegerField(editable=False, null=True, default=0)
    principleAmount = models.IntegerField()
    interestAmount = models.IntegerField()
    category = models.ForeignKey(loanCategorys, on_delete= models.CASCADE, null= True)
    loanNumber = models.CharField(max_length=20, unique=True, blank=False)
    reason=  models.TextField(default='loan')
    status = models.CharField(max_length=100, default='pending')
    term = models.IntegerField()
    appliedAt = models.DateTimeField(auto_now_add=True)
    interestRate = models.DecimalField(max_digits=4, decimal_places=2, default=2.00)

    def save(self, *args, **kwargs):
        # self.interestAmount = self.interestRate * self.principleAmount
        self.interestAmount = self.principleAmount * (self.interestRate / 100) * self.term
        self.totalAmount = self.principleAmount + self.interestAmount
        super(LoanApplication, self).save(*args, **kwargs)

    def __str__(self):
        # return f"{self.customer.firstName} {self.customer.lastName}"
        return f"Loan Application for {self.customerID}"
    

        
