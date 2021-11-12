from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import ChartData
from .parser import fetch_clien_latest_data

# Create your views here.
def main(request):
    return render(request, 'main.html')  

def chart(request):
    title = fetch_clien_latest_data()

    return render(request, 'chart.html', {'title': title})


def developers(request):
    return render(request, 'developers.html')
