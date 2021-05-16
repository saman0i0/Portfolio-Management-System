from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from authapp.models import Stock

@login_required(login_url='signin')
def home(request):
    return render(request, 'home.html')

def dashboard(request):
    stocks = Stock.objects.all()
    return render(request,'dashboard.html',{'stocks':stocks})

def addStock(request):
    return render(request,'form.html')

def addStockSubmission(request):
    
    company_name = request.POST.get("company_name",False)
    units = request.POST.get("units",False)
    buy_price = request.POST.get("buy_price",False)
    total_buy_price = int(units)*int(buy_price)
    curr_value = 1.3*total_buy_price
    profit = curr_value - total_buy_price
    
    stock_add_db =  Stock(company_name=company_name,units=units,
                             buy_price=total_buy_price,
                             curr_value=curr_value,
                             profit=profit)
    stock_add_db.save()
    print("Stock is added!!")
    return render(request,'home.html')