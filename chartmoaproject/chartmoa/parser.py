import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urlparse
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "ClienCrawlingDjango.settings") 
import django 
django.setup()

from chartmoa.models import ChartData


def fetch_clien_latest_data() :
    result = []
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))


    headers = {'Usr-Agent' : 'Mozilla/5.0 (Windows NT 10.0; win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://www.genie.co.kr/chart/top200'
    resp = requests.get(url, headers = headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    data = {}


    for song in songs:
         data = song.find('td',{'class':'info'}).find('a',{'class':'title ellipsis'}).text 
         result.append(data)
    
    return result

