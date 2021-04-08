from django.core.mail import message
from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_be5627477eda4219ab8663c382811c82")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

    # pk_be5627477eda4219ab8663c382811c82


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added to the portfolio")
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {'ticker': ticker})
