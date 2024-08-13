# myapp/signals.py
from django.db import IntegrityError
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from .models import LoanApplication
import uuid

@receiver(pre_save, sender=LoanApplication)
def generate_loan_number(sender, instance, **kwargs):
    if not instance.loanNumber:
        while True:
            loan_number = f"LN{uuid.uuid4().hex[:8].upper()}"
            if not LoanApplication.objects.filter(loanNumber=loan_number).exists():
                instance.loanNumber = "LN"+ loan_number
                break

@receiver(post_save, sender=LoanApplication)
def update_loan_status(sender, instance, **kwargs):
    if instance.status == 'Applied' and instance.appliedAt <= timezone.now() - timedelta(days=7):
        instance.status = 'Pending'
        instance.pendingAt = timezone.now()
        instance.save()