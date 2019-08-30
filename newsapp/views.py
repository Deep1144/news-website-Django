from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    import requests
    import time
    import json
    news = requests.get("https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=2a4aa639b670414e9c6f9d731ef7259e")

    news_text = news.text
    news_json = json.loads(news_text)

    # speak(news_json['articles'][0]["title"])

    return render(request,"index.html",{"news" : news_json})
    # return HttpResponse(news_json)

def speak(str):
    import win32com.client as win
    speak = win.Dispatch("SAPI.spVoice")
    speak.Speak(str)

