from django.urls import path
from Loan.views import LoanApplicationListCreateView, loanApplication
from Manager.models import loanCategorys


urlpatterns = [
    path('loan-applications/', LoanApplicationListCreateView.as_view(), name='loan-application-list-create'),
    path('loan-categories/', loanCategorys.as_view(), name='loan-application-list-create'),
    # path('', views.LoanApplicationList.as_view(), name='loan-application-list'),
    # path('<int:id>/', views.LoanApplicationDetail.as_view(), name='loan-application-detail'),
]
