from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/authentication/login')
def index(request):
    return render(request, 'expenses/index.html')


@login_required(login_url='/authentication/login')
def add_expense(request):
    return render(request, 'expenses/add_expense.html')

