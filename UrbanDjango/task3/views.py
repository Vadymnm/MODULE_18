from django.shortcuts import render
from django.views.generic import TemplateView


# def index(request):
#     return render(request, 'platform.html')


#from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Главная страница'
    context = {
        'title': title,
        'main': "Главная",
        'shop': "Магазин",
        'bask': "Корзина", }
    return render(request, 'platform.html',context)


def games(request):
    title = 'ИГРЫ:'
    context = {
        'title': title,
        'first': "1 - Atomic Heart ",
        'second': "2 - Cyberpunk ",
        'third': "3 - PayDay ", }
    return render(request, 'games.html',context)