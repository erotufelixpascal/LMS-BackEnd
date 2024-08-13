from django.apps import AppConfig

class LoanConfig(AppConfig):
    name = 'Loan'

    def ready(self):
        import Loan.signals

