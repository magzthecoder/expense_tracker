from django import forms
from .models import Category, Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_name','expense_price','date_bought','category']