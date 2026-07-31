from django.db import models

# Create your models here.
class sif(models.Model):
    name = models.CharField(max_length=100)
    enrollment = models.CharField(max_length=100)
    roll = models.IntegerField()
    dob = models.DateField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
