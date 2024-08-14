from django.http import JsonResponse
from django.shortcuts import render
from Loan.models import LoanApplication, Payment
from rest_framework import generics
from rest_framework.response import Response
from Loan.serializers import LoanApplicationSerializer, LoanSerializer, PaymentSerializer
from datetime import timedelta

# Create your views here.
    
class LoanApplicationListCreateView(generics.ListCreateAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer

class LoansListCreateView(generics.ListCreateAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanSerializer

class ScheduleViewSet(generics.ListCreateAPIView):
    queryset = Payment.objects.all().order_by('loanNumber')
    serializer_class = PaymentSerializer

    # def perform_create(self, serializer):
    def perform_create(self,request):
        payment = request.save()
        schedule = []
        # Loan details
        loan_amount = payment.totalAmount
        # interest_rate = Payment.interest / 12  # Convert annual rate to monthly
        interest_rate = payment.interest # Convert annual rate to monthly
        term_in_months = payment.term
        # term_in_months = 4

        # Calculate EMI(Equated Monthly Installment)
        emi = (loan_amount * interest_rate * (1 + interest_rate)**term_in_months) / ((1 + interest_rate)**term_in_months - 1)
        balance = loan_amount

        for month in range(term_in_months):
            interest_payment = balance * interest_rate
            principal_payment = emi - interest_payment
            balance -= principal_payment
        
            # Create repayment schedule entry
            # Payment.objects.create(
            #     # loanNumber
            #     totalAmount =emi,
            #     principal =principal_payment,
            #     interest = interest_payment,
            #     balance =balance,
            #     payment_date=LoanApplication.disbursedAt,
            #     next_payment_date=LoanApplication.disbursedAt,
            #     # payment_date =loan.start_date + timedelta(days=30*(month+1)),
            #     # next_payment_date =loan.start_date + timedelta(days=30*(month+1))    
            #     # installment_number=month + 1,
            # )
            # schedule.append(Payment)
            schedule.append({
                'totalAmount':emi,
                'principal':principal_payment,
                'interest': interest_payment,
                'balance':balance,
                'payment_date':LoanApplication.disbursedAt,
                'next_payment_date':LoanApplication.disbursedAt,
                # 'Month': month + 1,
                # 'installment_number'=month + 1
            })

        return Response(schedule)

class PaymentViewSet(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


# class ScheduleViewSet(generics.ListCreateAPIView):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer

#     # def generate_repayment_schedule(self,principal, annual_rate, years):
#     def generate_repayment_schedule(self):
#         schedulePayments = Payment.objects.all()

#         # monthly_rate = annual_rate / 12 / 100
#         # num_payments = years * 12
#         # monthly_payment = (principal * monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
#         # remaining_balance = principal
#         schedule = []

#         for schedules in schedulePayments:
#             # for i in range(num_payments):
#             #     interest_payment = remaining_balance * monthly_rate
#             #     principal_payment = monthly_payment - interest_payment
#             #     remaining_balance -= principal_payment
#                 schedule.append({
#                     'Loan Number':schedules.loanNumber,
#                     'Total Amount': schedules.totalAmount,
#                     'principal': schedules.principal,
#                     'Interest': schedules.interest,
#                     'balance': schedules.balance,
#                     'payment_date': schedules.payment_date,
#                     'next_payment_date': schedules.next_payment_date,
#                     # 'Month': i + 1,
#                     # 'Monthly Payment': round(monthly_payment, 2),
#                     # 'Principal Payment': round(principal_payment, 2),
#                     # 'Interest Payment': round(interest_payment, 2),
#                     # 'Remaining Balance': round(remaining_balance, 2)
#                 })
            
#         return schedule
        
#     def get(self, request, *args, **kwargs):
#         schedule = self.generate_repayment_schedule()
#         return Response(schedule)

