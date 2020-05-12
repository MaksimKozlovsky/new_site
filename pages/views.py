from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import os
from pages.models import Pages
from django.contrib.auth import get_user_model


def index(request):

    my_pages = Pages.objects.all()
#    page_id = Pages.objects.get(pk=request.GET.filter('id'))
    page_id = request.GET.get('id')
    if page_id:
        page = Pages.objects.get(pk=request.GET.get('id'))
        context = {'page': page}
    else:
        my_pages = Pages.objects.all()
        context = {'pages': my_pages}
    return render(request, 'index.html', context=context)



def Onliner(request):


    my_article = []
    my_article.append({'title': 'News', 'text': 'бла бла'})
    my_article.append({'title': 'News', 'text': 'бла бла бла'})

    context = {
        'title': 'Страница Onliner',
        'list_of_article': my_article
    }
    return render(request, 'Onliner.html', context=context)

def Telegram(request):


    my_article = []
    my_article.append({'title': 'News', 'text': 'super бла'})
    my_article.append({'title': 'News', 'text': 'super бла бла'})

    context = {
        'title': 'Страница Telegram',
        'list_of_article': my_article
    }
    return render(request, 'Telegram.html', context=context)

def user_registration(request):
    User = get_user_model()
    new_user = User(request.POST.get('all'))
    new_user.set_password(request.POST.get('password'))
    new_user.save()
    context = {"new_user": new_user}
    return render(request, 'index.html', context=context)