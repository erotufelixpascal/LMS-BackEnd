from django.apps import AppConfig


class LoanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Loan'

    def ready(self):
        # import Loan.Signals;
        # import Loan.models.Signals
        import Loan.signals

