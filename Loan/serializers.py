# serializers.py
from rest_framework import serializers
from .models import LoanApplication, Payment

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ['loanNumber']

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = '__all__'  # Or list the specific fields you want to serialize

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

        def create(self, validated_data):
            loan_application = LoanApplication.objects.get(id=validated_data['loanNumber'].id)
            payment = Payment.objects.create(
                loanNumber=loan_application,
                totalAmount=validated_data['totalAmount'],
                principal=validated_data['principal'],
                interest=validated_data['interest'],
                balance=validated_data['balance'],
                term=validated_data['term'],
                payment_date=validated_data['payment_date'],
                next_payment_date=validated_data['next_payment_date']
            )
            return payment
