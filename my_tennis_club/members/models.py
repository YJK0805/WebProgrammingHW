from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    age = models.IntegerField(null=True, default=50)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"  

# Create court model
class Court(models.Model):
    name = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.types} {self.location}"
