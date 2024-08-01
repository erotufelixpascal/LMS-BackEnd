from Loan.models import LoanApplication
from Manager.models import Users, loanCategorys, loanTerms, loanUsers
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class loanCategorysSerializer(serializers.ModelSerializer):
    class Meta:
        model = loanCategorys
        fields = '__all__'  # Or list the specific fields you want to serialize

class loanUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = loanUsers
        fields = '__all__'  # Or list the specific fields you want to serialize

class loanTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = loanTerms
        fields = '__all__'  # Or list the specific fields you want to serialize

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ['loanNumber', 'status']
        # fields = '__all__'

class LoanStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = '__all__'

# ##here starts a new

# class UserRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = loanUsers
#         fields = ['userType']

# class UserSerializer(serializers.ModelSerializer):
#     userRole = serializers.SerializerMethodField()

#     class Meta:
#         model = Users
#         fields = ['customerID', 'firstName', 'lastName', 'email', 'address', 'designation', 'phone', 'information', 'userRole']

#     def get_userRole(self, obj):
#         try:
#             user_role = loanUsers.objects.get(id=obj.userRole)
#             return user_role.userType
#         except loanUsers.DoesNotExist:
#             return None