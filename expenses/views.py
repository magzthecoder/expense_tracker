from django.shortcuts import render,redirect
from .models import Category, Expense
from .forms import ExpenseForm
from django.contrib import messages


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

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST,user=request.user)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, "Expense added successfully")
            return redirect('expense_list')
    else:
        form = ExpenseForm(user=request.user)
    context = {
        'form':form
    }
    return render(request,'add_expense.html',context)
    
