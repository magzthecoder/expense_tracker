from django import forms
from .models import Category, Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_name','expense_price','date_bought','category']

    def __init__(self,*args,user=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show categories owned by the currently logged-in user in the task form dropdown
        self.fields['category'].queryset = Category.objects.filter(user=user)