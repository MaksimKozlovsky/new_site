from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import os
from pages.models import Pages, Comment
from pages.forms import RegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
User = get_user_model()



def index(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        page = Pages.objects.get(pk=request.GET.get('id'))
        comment = Comment(text=comment, author=request.user, page=page)
        comment.save()
        comments = Comment.objects.filter(page=page)
        context = {'page': page,
                   'comments': comments
                   }
    else:
        page_id = request.GET.get('id')
        if page_id:
            page = Pages.objects.get(pk=request.GET.get('id'))
            comments = Comment.objects.filter(page=page)
            context = {'page': page,
                       'comments': comments
                       }
        else:
            my_pages = Pages.objects.all()
            comments = Comment.objects.filter(page=my_pages)
            context = {'pages': my_pages,
                       'comments': comments
                       }
    return render(request, 'index.html', context=context)




def login_up(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login_up.html', context=context)


def registration(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        else:
            return redirect('/')
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            User.objects.create_user(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                username=form.cleaned_data['email']
            )
            return redirect('/')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'login_up.html', context=context)



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

