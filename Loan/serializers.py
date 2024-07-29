# serializers.py
from rest_framework import serializers
from .models import LoanApplication

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = '__all__'  # Or list the specific fields you want to serialize

# class LoanSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LoanApplication
#         fields = ['loanNumber', 'status']
