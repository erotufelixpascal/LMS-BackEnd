from django.urls import path
from Manager.serializers import loanTermSerializer
from Manager.views import CustomerListCreateView, loanCategoryListCreateView, loanUsersSerializer

urlpatterns = [
    path('Users/', CustomerListCreateView.as_view(), name='user-roles'),
    path('loan-categories', loanCategoryListCreateView.as_view(), name='loan-categories'),
    path('user-roles', loanUsersSerializer.as_view(), name='user-roles'),
    path('loan-terms', loanTermSerializer.as_view(), name='loan-terms'),
]