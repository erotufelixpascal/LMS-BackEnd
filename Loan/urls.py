from django.urls import path
from Loan.views import LoanApplicationListCreateView, ScheduleViewSet, loanApplication
from Manager.models import loanCategorys


urlpatterns = [
    path('loan-applications/', LoanApplicationListCreateView.as_view(), name='loan-application-list-create'),
    path('loan-categories/', loanCategorys.as_view(), name='loan-application-list-create'),
    path('loan/<int:loan_id>/schedule/', ScheduleViewSet.as_view(), name='loan-schedule'),
    # path('', views.LoanApplicationList.as_view(), name='loan-application-list'),
    # path('<int:id>/', views.LoanApplicationDetail.as_view(), name='loan-application-detail'),
]
