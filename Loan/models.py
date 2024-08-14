from datetime import timedelta
import uuid
from django.db import IntegrityError, models
import Loan
from Manager.models import Users, loanCategorys
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from dateutil.relativedelta import relativedelta


# default_customer = Users.objects.first()  ,default=default_customer- '18c8ca88c8834e4e921d007110232d74'

# Create your models here.
class LoanApplication(models.Model):
    customerID = models.ForeignKey(Users, on_delete = models.CASCADE, related_name='loan_user' )
    totalAmount = models.IntegerField(editable=False, null=True, default=0)
    principalAmount = models.IntegerField()
    interestAmount = models.IntegerField()
    category = models.ForeignKey(loanCategorys, on_delete= models.CASCADE, null= True)
    loanNumber = models.CharField(max_length=20, unique=True, blank=False)
    reason=  models.TextField(default='loan')
    status = models.CharField(max_length=100, default='Pending')
    term = models.IntegerField() #in months
    appliedAt = models.DateTimeField(auto_now_add=True)
    interestRate = models.DecimalField(max_digits=4, decimal_places=2, default=2.00)
    disbursedAt = models.DateTimeField(null=True, blank=True)
    recoveredAt = models.DateTimeField(null=True, blank=True)
    pendingAt = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # self.interestAmount = self.interestRate * self.principleAmount
        self.interestAmount = self.principalAmount * (self.interestRate / 100) * self.term
        self.totalAmount = self.principalAmount + self.interestAmount
        # self.balance = self.totalAmount -  (self.)
        super(LoanApplication, self).save(*args, **kwargs)

    def __str__(self):
        # return f"{self.customer.firstName} {self.customer.lastName}"
        return f"Loan Application for {self.customerID}"
    

class Payment(models.Model):
    loanNumber = models.ForeignKey(LoanApplication, on_delete=models.CASCADE, related_name='loan_number')
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    principal = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    term = models.IntegerField(default=1) #in months
    payment_date = models.DateTimeField(default=timezone.now)
    next_payment_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.totalAmount = self.principal + self.interest
        self.balance = self.balance - self.principal
        self.next_payment_date = self.payment_date + relativedelta(months=self.term)
        
        super(Payment, self).save(*args, **kwargs)
    
# @shared_task
    def deduct_loan_payments():
        loans = Payment.objects.filter(next_payment_date__lte=timezone.now())
        for loan in loans:
            # Assuming equal monthly payments
            monthly_payment = calculate_monthly_payment(LoanApplication)
            loan.balance -= monthly_payment
            loan.next_payment_date += timedelta(days=30)  # Move to next payment date
            loan.save()
    
        def calculate_monthly_payment(self,_loan_application):
                rate = LoanApplication.interestRate / 100 / 12
                term = LoanApplication.term
                principal = Payment.principal
                totalAmount = principal * (rate * (1 + rate) ** term) / ((1 + rate) ** term - 1)
                return totalAmount

    def generate_repayment_schedule(self, principal, annual_rate, years):
            monthly_rate = annual_rate / 12 / 100
            num_payments = years * 12
            # monthly_payment = (principal * monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
            monthly_payment = calculate_monthly_payment(LoanApplication)
            schedule = []
            remaining_balance = principal

            def calculate_monthly_payment(self,_loan_application):
                    rate = LoanApplication.interestRate / 100 / 12
                    term = LoanApplication.term
                    principal = Payment.principal
                    totalAmount = principal * (rate * (1 + rate) ** term) / ((1 + rate) ** term - 1)
                    return totalAmount

            for i in range(num_payments):
                interest_payment = remaining_balance * monthly_rate
                principal_payment = monthly_payment - interest_payment
                remaining_balance -= principal_payment
                schedule.append({
                    'Month': i + 1,
                    'Monthly Payment': round(monthly_payment, 2),
                    'Principal Payment': round(principal_payment, 2),
                    'Interest Payment': round(interest_payment, 2),
                    'Remaining Balance': round(remaining_balance, 2)
                })
            
            return schedule
    
    # schedule = generate_repayment_schedule(100000, 5, 15)
    # for payment in schedule:
    #         print(payment)



        
        

    

        
