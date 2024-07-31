from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from Loan.models import LoanApplication
# from Loan.serializers import LoanSerializer
from Manager.models import Users, loanCategorys, loanTerms, loanUsers
from Manager.serializers import LoanSerializer, LoanStatisticsSerializer, UserSerializer, loanCategorysSerializer, loanTermSerializer,loanUsersSerializer
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
# class UserRoleView(View):
#     def get(self, request):
#         # Your logic to get user roles
#         roles = ["admin", "user", "guest"]
#         return JsonResponse({"roles": roles})

# class loanCategory(View):
#     def get(self, request):
#         loanNames = loanCategorys.objects.values_list('loanName', flat = True)
#         return JsonResponse(list(loanNames), safe= False)
    
class loanCategoryListCreateView(generics.ListCreateAPIView):
    queryset = loanCategorys.objects.all()
    serializer_class = loanCategorysSerializer

class loanUsersListCreateView(generics.ListCreateAPIView):
    queryset = loanUsers.objects.all()
    serializer_class = loanUsersSerializer

class loanTermListCreateView(generics.ListCreateAPIView):
    queryset = loanTerms.objects.all()
    serializer_class = loanTermSerializer

class LoanViewSet(generics.ListCreateAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
    
class UserRoleView(generics.ListCreateAPIView):
    def get(self, request, userRole):
        user_roles = Users.objects.filter(userRole=userRole)
        user_roles_list = list(user_roles.values())
        return JsonResponse(user_roles_list, safe=False)
    
class UserDetail(generics.ListCreateAPIView):
    # queryset = Users.objects.all()
    # serializer_class = UserSerializer
    # lookup_field = 'customerID'
    def get(self, request, email):
        user_detail = Users.objects.filter(email=email)
        user_detail_list = list(user_detail.values())
        return JsonResponse(user_detail_list, safe=False)

#returning http://127.0.0.1:8000/users?userRole=5
class UserViewSet(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_role = self.request.query_params.get('userRole')
        if user_role is not None:
            queryset = queryset.filter(userRole=user_role)
        return queryset
    
#returning statistics
class LoanStatisticsView(generics.ListCreateAPIView):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanStatisticsSerializer

    def get(self, request):
        loans_applied = LoanApplication.objects.filter(status='Applied').count()
        loans_disbursed = LoanApplication.objects.filter(status='Disbursed').count()
        loans_recovered = LoanApplication.objects.filter(status='Recovered').count()
        loans_pending = LoanApplication.objects.filter(status='Pending').count()
        
        data = {
            'loans_applied': loans_applied,
            'loans_disbursed': loans_disbursed,
            'loans_recovered': loans_recovered,
            'loans_pending': loans_pending
        }
        
        return Response(data)