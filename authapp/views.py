from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Stock

from .forms import LoginForm, RegistrationForm      

def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    context = {
        'form': forms
    }
    return render(request, 'signin.html', context)


def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    return redirect('signin')
                except:
                    context = {
                        'form': forms,
                        'error': 'This Username Already exists!'
                    }
                    return render(request, 'signup.html', context)
    context = {
        'form': forms
    }
    return render(request, 'signup.html', context)

def signout(request):
    logout(request)
    return redirect('signin')

def addStockSubmission(request):
    
    company_name = request.POST["company_name"]
    units = request.POST["units"]
    buy_price = request.POST["buy_price"]
    total_buy_price = int(units)*int(buy_price)
    curr_value = 1.3*total_buy_price
    profit = curr_value - total_buy_price
    
    stock_add_db =  Stock(company_name=company_name,units=units,
                             buy_price=total_buy_price,
                             curr_value=curr_value,
                             profit=profit)
    stock_add_db.save()
    print("Form is submitted!!")
    return render(request,'home.html')