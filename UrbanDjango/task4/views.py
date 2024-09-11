
from django.shortcuts import render
from django.views.generic import TemplateView


def main(request):
    title = 'Главная страница'
    context = {
        'title': title,
        'main': "Главная",
        'shop': "Магазин",
        'bask': "Корзина", }
    return render(request, 'menu.html',context)


def games(request):
    games_list = ["World of tanks", "Tetris", "Atomic Heart", "Cyberpunk", "PayDay" ]
    context = {
        'games_list': games_list,
         }
    return render(request, 'games.html', context)

