# myapp/signals.py
from django.db import IntegrityError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import LoanApplication
import uuid

@receiver(pre_save, sender=LoanApplication)
def generate_loan_number(sender, instance, **kwargs):
    # if created and not instance.loanNumber:
    #     while True:
    #         loanNumber = f"LN{uuid.uuid4().hex[:8].upper()}"
    #         if not LoanApplication.objects.filter(loanNumber=loanNumber).exists():
    #             instance.loanNumber = loanNumber
    #             try:
    #                 instance.save()
    #                 break
    #             except IntegrityError:
    #                 continue
    if not instance.loanNumber:
        while True:
            loan_number = f"LN{uuid.uuid4().hex[:8].upper()}"
            if not LoanApplication.objects.filter(loanNumber=loan_number).exists():
                instance.loanNumber = "LN"+ loan_number
                break