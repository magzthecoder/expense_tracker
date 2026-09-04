from django.db import models
from django.contrib.auth.models import User
from django.db.models import UniqueConstraint

class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.category
    
    class Meta:
        constraints =[
            UniqueConstraint(fields=["category","user"], name="unique_category")
        ]
        verbose_name_plural = "Categories"

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    expense_name = models.CharField(max_length=100,null=False)
    expense_price = models.DecimalField(max_digits=9,decimal_places=2)
    date_bought = models.DateField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.expense_name