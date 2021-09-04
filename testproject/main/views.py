from django.shortcuts import render


def index(requests):
    data = {
        'title': 'Главная страница'
    }
    return render(requests, 'main/index.html', data)


def about(requests):
    return render(requests, 'main/about.html')
