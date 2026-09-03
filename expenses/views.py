from django.shortcuts import render
from .models import Category, Expense
from django.contrib.auth.models import User

def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    context = {
        'expenses':expenses
    }
    return render(request,'expense_list.html',context)

def expense_detail(request,id):
    expense = Expense.objects.get(id=id,user=request.user)
    context = {
        'expense':expense
    }
    return render(request,'expense_detail.html',context)

    
