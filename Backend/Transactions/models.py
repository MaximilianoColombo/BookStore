from django.db import models
from Backend.Members.models import Member
from Backend.Books.models import Book

# Create your models here.

    
class Transaction (models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    loanDate = models.DateField(auto_now_add=True)
    cost = models.FloatField(default=0)
    returnDate = models.DateField(null=True, blank=True)
    loanStatusChoices = [
        ("inCourse", "En curso"),
        ("returned", "Devuelto"),
    ] 
    loanStatus = models.CharField(choices=loanStatusChoices, max_length=20, default="inCourse")

    class Meta:
        ordering = ['member', 'loanDate', 'loanStatus']
