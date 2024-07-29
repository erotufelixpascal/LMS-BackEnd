from django.contrib import admin
from Manager.models import loanTerms, loanUsers, loanCategorys,Users

# Register your models here.

admin.site.register(loanUsers)
admin.site.register(loanCategorys)
admin.site.register(Users)
admin.site.register(loanTerms)
