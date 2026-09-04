from django import forms
from .models import Category, Expense
from django.core.exceptions import ValidationError

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_name','expense_price','date_bought','category']

    def __init__(self,*args,user=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show categories owned by the currently logged-in user in the task form dropdown
        self.fields['category'].queryset = Category.objects.filter(user=user)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

    def __init__(self,*args,user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.user=user

    def clean(self): #Checks if category exists already
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        user = self.instance.user

        if category:
            # Only do something if both fields are valid so far.
            if Category.objects.filter(user=user,category=category).exists():
                raise ValidationError(
                    "Category Already Exists"
                )
            else:
                return cleaned_data