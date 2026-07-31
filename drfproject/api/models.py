from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField()
    location=models.CharField()
    year=models.IntegerField()
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    e_name=models.CharField()
    salary=models.IntegerField()
    des=models.CharField()
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.e_name