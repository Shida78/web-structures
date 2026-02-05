from django.shortcuts import render
from django.http import HttpResponse

# request — это "письмо" от браузера с данными о пользователе
def home(request):
    # 1. Готовим данные (Context). Это словарь Python.
    # Ключи словаря станут именами переменных в HTML.
    context_data = {
    'page_title': 'Главная Галерея',
    'models_count': 0, # Попробуйте поменять на 5, чтобы проверить условие
    }

    # 2. Рендерим (смешиваем HTML и данные)
    # Путь указываем относительно папки templates: 'gallery/index.html'
    return render(request, 'gallery/index.html', context_data)

def about(request):
    # Мы пока не используем HTML-шаблоны, просто вернем строку.
    return HttpResponse("<h1>Курс Web Структуры</h1><p>Здесь мы делаем сайт типо Scetchfab.</p>")
