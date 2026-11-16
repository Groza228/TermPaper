from django.shortcuts import render
from news.models import Articles


def index(request):
    news = Articles.objects.order_by('-id')[:3]
    data = {
        'title': 'Головна сторінка',
        'news': news
    }
    return render(request, 'main/index.html', data)


def about(request):

    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

