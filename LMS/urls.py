"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Loan import views as loan_views
from Manager import views as manager_views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'users', manager_views.UserViewSet)


urlpatterns = [
    # path('tests', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('users', manager_views.CustomerListCreateView.as_view()),
    path('users/<str:customerID>/', manager_views.UserDetail.as_view(), name='user-detail'),
    # path('users/customerID/', manager_views.UserDetail.as_view(), name='user-detail'),
    path('user-roles', manager_views.loanUsersListCreateView.as_view(), name='user-roles'),
    path('loan-categories', manager_views.loanCategoryListCreateView.as_view()),
    path('loan-terms', manager_views.loanTermListCreateView.as_view()),
    path('loan-application', loan_views.LoanApplicationListCreateView.as_view()),
    # path('loan-application/?status=pending', manager_views.LoanViewSet.as_view()),
    path('loan-application/pending', manager_views.LoanViewSet.as_view()),
    path('loan-application/approved', manager_views.LoanViewSet.as_view()),
    path('loan-application/disbursed', manager_views.LoanViewSet.as_view()),
    path('user-roles/<str:userType>/', manager_views.UserRoleView.as_view(), name='user-roles'),
    path('users', manager_views.UserViewSet.as_view(), name='user-roles-roles'),
    path('loan-statistics/', manager_views.LoanStatisticsView.as_view(), name='loan-statistics'),
    path('', loan_views.LoanApplicationListCreateView.as_view())

]
