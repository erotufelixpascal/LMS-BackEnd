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
#returning http://127.0.0.1:8000/statistics?userRole=5
# GET /loan-statistics/?staff_id=1
# http://127.0.0.1:8000/loans?userRole=5
class LoanStatisticsView(generics.ListCreateAPIView):
    serializer_class = LoanStatisticsSerializer

    def get(self, request, *args, **kwargs):
        user_role = request.query_params.get('userRole', None)
        if user_role is not None:
            loans_data = LoanApplication.objects.filter(customerID__userRole=user_role)
        else:
            loans_data = LoanApplication.objects.all()
    
        if user_role is not None:
            users_data = Users.objects.filter(userRole=user_role)
        else:
            users_data = Users.objects.all()

        loan_serialized = LoanSerializer(loans_data, many=True)

        response_data = []

        for user in users_data:
            loans_data = LoanApplication.objects.filter(customerID=user)

            loans_applied = loans_data.filter(status='Applied').count()
            loans_disbursed = loans_data.filter(status='Disbursed').count()
            loans_recovered = loans_data.filter(status='Recovered').count()
            loans_pending = loans_data.filter(status='Pending').count()

            total_loans_handled = loans_applied + loans_disbursed + loans_recovered + loans_pending

            if total_loans_handled > 0:
                effectiveness = ((loans_disbursed + loans_recovered) / total_loans_handled) * 100
            else:
                effectiveness = 0

            user_data = {
                'customerID': user.customerID,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'email': user.email,
                'address': user.address,
                'designation': user.designation,
                'phone': user.phone,
                'information': user.information,
                # 'userRole': user.userRole,
                # 'loans': LoanSerializer(loans_data, many=True).data,
                'loans': loan_serialized.data,
                'loans_applied': loans_applied,
                'loans_disbursed': loans_disbursed,
                'loans_recovered': loans_recovered,
                'loans_pending': loans_pending,
                'effectiveness': effectiveness
            }

            response_data.append(user_data)
        return Response(response_data)

            
