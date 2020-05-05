from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


def index(request):
    my_article = []
    my_article.append({'title': 'Onliner', 'text': 'Оцени логотип'})
    my_article.append({'title': 'Telegram', 'text': 'Оцени логотип'})

    context = {
        'title': 'Страница Onliner',
        'title': 'Страница Telegram',
        'list_of_article': my_article
    }
    return render(request, 'index.html', context=context)


def Onliner(request):


    my_article = []
    my_article.append({'title': 'Onliner', 'text': 'Голосуем за логотип'})
    my_article.append({'title': 'Onliner', 'text': 'Предложи свой вариант'})

    context = {
        'title': 'Страница Onliner',
        'list_of_article': my_article
    }
    return render(request, 'Onliner.html', context=context)

def Telegram(request):


    my_article = []
    my_article.append({'title': 'Telegram', 'text': 'Голосуем за логотип'})
    my_article.append({'title': 'Telegram', 'text': 'Предложи свой вариант'})

    context = {
        'title': 'Страница Telegram',
        'list_of_article': my_article
    }
    return render(request, 'Telegram.html', context=context)
