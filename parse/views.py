import requests
import json

from django.shortcuts import render, HttpResponseRedirect


def index(request):
    return render(request, 'index.html')

def coingecko(request):
    try:
        with open('./coingecko.json', 'r', encoding='utf-8') as f:
            templates = json.load(f)
            message = ''
    except:
        message = 'Нажмите запрос coingecko'
        templates = ''
    return render(request, 'coingecko.html', context={'templates': templates, 'message': message})

def create_coingecko(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=65&page=1&sparkline=false'
    response = requests.get(url)
    json_data = json.loads(response.text)
    with open('./coingecko.json', 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=1)
    return HttpResponseRedirect('/coingecko')

def cryptorank(request):
    try:
        with open('./cryptorank.json', 'r', encoding='utf-8') as f:
            templates = json.load(f)
            message = ''
    except:
        message = 'Нажмите запрос cryptorank'
        templates = ''
    return render(request, 'cryptorank.html', context={'templates': templates, 'message': message})

def create_cryptorank(request):
    url = 'https://api.cryptorank.io/v1/currencies?limit=3&api_key= '
    response = requests.get(url)
    json_data = json.loads(response.text)
    data = json_data['data']
    with open('./cryptorank.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    return HttpResponseRedirect('/cryptorank')
