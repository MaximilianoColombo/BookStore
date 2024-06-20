from django.db import models
from django.core.validators import RegexValidator

class Member(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber = models.CharField(
        validators=[RegexValidator(regex='^\d+$', message='El número de celular solo debe contener dígitos.')], 
        max_length=20)
