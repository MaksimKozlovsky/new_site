from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import os
from pages.models import Pages


def index(request):

    my_pages = Pages.objects.all()
#    page_id = Pages.objects.get(pk=request.GET.filter('id'))
    page_id = request.GET.get('id')
    if page_id:
        Pages.objects.get(pk=request.GET.get('id'))
    else:
        Pages.objects.filter(pk=request.GET.get('id'))
    context = {'pages': my_pages,
#               'pages': page_id
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
