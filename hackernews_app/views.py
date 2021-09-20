from django.shortcuts import render, redirect

import datetime, requests, json

from .models import News
from .forms import NewsForm



def index(request):
    news = News.objects.all()
    form = NewsForm()

    res = requests.get(
        'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty').json()
    
    top_news = []
    news_type = []

    for item in res[0:5]:
        info= requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty')
        top_news.append(json.loads(info.text))
        news_type.append(json.loads(info.text)['type'])
    
    types = set(news_type)

    
    context = {"news": news, "form": form, "items":item, "top_news":top_news, "types":types}
    return render(request, 'app/index.html', context)
