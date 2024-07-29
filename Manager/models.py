from django.db import models
import uuid

# Create your models here.
class loanUsers(models.Model):
    userType = models.CharField(max_length=250)
    creationDate =models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.userType

class Users(models.Model):
    customerID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length= 250, blank=False)
    lastName = models.CharField(max_length =250, blank= False)
    email = models.EmailField(max_length= 100, blank =False)
    userRole = models.ForeignKey(loanUsers, on_delete= models.CASCADE, null= True)
    # userRole = models.CharField(max_length=100)
    address =models.CharField(max_length=250, default='Soroti,Uganda', blank= True, null= True)
    designation = models.CharField(max_length=250, blank= False)
    phone =models.IntegerField(blank=True, null=True)
    information= models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    
#calculating effectiveness
# class Staff(models.Model):
#     userRole = models.ForeignKey(Users, on_delete= models.CASCADE, null= True)
#     firstName = models.ForeignKey(Users, on_delete= models.CASCADE, null= True)
#     lastName = models.ForeignKey(Users, on_delete= models.CASCADE, null= True)
#     applied = models.IntegerField(blank=True, null=True)
#     disubursed = models.IntegerField(blank=True, null=True)
#     recovered = models.IntegerField(blank=True, null=True)
#     effectiveness = models.IntegerField(blank=True, null=True)

#     def save(self, *args, **kwargs):
#         self.applied = self.applied * (self.applied / 100) * self.applied
#         self.disubursed = self.applied * (self.applied / 100) * self.applied
#         self.recovered = self.applied * (self.applied / 100) * self.applied
#         self.effectiveness = self.applied + self.applied
#         super(Staff, self).save(*args, **kwargs)

    
class loanCategorys(models.Model):
    loanName= models.CharField(max_length=250)
    creationDate =models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.loanName
    
class loanTerms(models.Model):
    loanType= models.CharField(max_length=250)
    typicalPeriod= models.CharField(max_length=500)
    commonUseCases= models.CharField(max_length=500)
    creationDate =models.DateField(auto_now_add=True)
    updatedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.loanType


