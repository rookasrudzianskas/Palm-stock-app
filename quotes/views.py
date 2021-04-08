from django.shortcuts import render


def home(request):
    import requests
    import json

    api_request = requests.get(
        "https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_be5627477eda4219ab8663c382811c82")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    # pk_be5627477eda4219ab8663c382811c82

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
