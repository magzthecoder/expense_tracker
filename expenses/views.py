from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Expense
from .forms import ExpenseForm, CategoryForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    context = {
        'expenses':expenses
    }
    return render(request,'expense_list.html',context)

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    context = {
        'categories':categories,
        'expenses':expenses
    }
    return render(request,'category_list.html',context)

@login_required
def expense_detail(request,id):
    expense = get_object_or_404(Expense,id=id,user=request.user)
    context = {
        'expense':expense
    }
    return render(request,'expense_detail.html',context)

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST,user=request.user)
        if form.is_valid():
            expense = form.save(commit=False) #dont save expense into database yet
            expense.user = request.user # attach expense to a user
            expense.save() #now save expense into database since it has user
            messages.success(request, "Expense added successfully")
            return redirect('expense_list')
    else:
        form = ExpenseForm(user=request.user)
    context = {
        'form':form
    }
    return render(request,'add_expense.html',context)

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST,user=request.user)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, "Category Added")
            return redirect('add_expense')
    else:
        form = CategoryForm(user=request.user)
    context = {
        'form':form
    }
    return render(request,'add_category.html',context)

@login_required
def update_expense(request,id):
    expense = get_object_or_404(Expense,id=id,user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense Updated")
            return redirect ('expense_detail',id=expense.id)
    else:
        form = ExpenseForm(instance=expense ,user=request.user)
    context = {
        'form':form
    }
    return render(request,'add_expense.html',context)

@login_required
def delete_expense(request,id):
    expense = get_object_or_404(Expense,id=id,user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.info(request, "Expense Deleted")
        return redirect('expense_list')
    context = {
        'expense':expense
    }
    return render(request, 'delete_expense.html',context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or Password")
            return redirect('login_page')
        else:
            login(request,user)
            return redirect('expense_list')
    return render (request,'login.html')

def logout_page(request):
    logout(request)
    messages.info(request, "You are logged out")
    return redirect('login_page')

def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect('register_page')

        user = User.objects.create_user(
            email=email,
            username=username,
            password=password
        )
        login(request, user)
        messages.info(request, "Account created successfully")
        return redirect('expense_list')
    return render(request,'register_page.html')

@login_required
def search_expense(request):
    query = request.GET.get('q', '')
    expenses = Expense.objects.filter(user=request.user)
    category = Category.objects.filter(user=request.user)

    if query:
        expenses = expenses.filter(
            Q(expense_name__icontains=query) | Q(category__category__icontains=query))
    context = {
        'expenses':expenses,
        'query':query
    }
    return render(request,'expense_list.html',context)
