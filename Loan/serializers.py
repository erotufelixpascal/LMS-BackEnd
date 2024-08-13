# serializers.py
from rest_framework import serializers
from .models import LoanApplication, Payment

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = '__all__'  # Or list the specific fields you want to serialize

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
