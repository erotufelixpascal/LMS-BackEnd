from django.contrib import admin
from Loan.models import LoanApplication,Payment

# Register your models here.
admin.site.register(LoanApplication)
admin.site.register(Payment)