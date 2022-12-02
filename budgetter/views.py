from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'budgetter/index.html')

def add_expense(request):
    return render(request, 'budgetter/add_expense.html')
