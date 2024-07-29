from django.http import JsonResponse
from django.shortcuts import render
from Loan.models import LoanApplication
from rest_framework import generics
from Loan.serializers import LoanApplicationSerializer

# Create your views here.
    
class LoanApplicationListCreateView(generics.ListCreateAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer

# class LoanViewSet(generics.ListCreateAPIView):
#     queryset = LoanApplication.objects.all()
#     serializer_class = LoanSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         status = self.request.query_params.get('status')
#         if status:
#             queryset = queryset.filter(status=status)
#         return queryset