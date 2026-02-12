from django.shortcuts import render
from .models import Asset # Импортируем модель, чтобы спрашивать данные

# request — это "письмо" от браузера с данными о пользователе
def home(request):
   # ORM Запрос: "Дай мне все объекты Asset из базы"
    assets = Asset.objects.all()
    
    context_data = {
    'page_title': 'Главная Галерея',
    'assets': assets, # Передаем реальный QuerySet (список)
    }

    return render(request, 'gallery/index.html', context_data)

def about(request):
    context_data = {
    #'page_title': 'О нас',
    }
    # Мы пока не используем HTML-шаблоны, просто вернем строку.
    #return HttpResponse("<h1>Курс Web Структуры</h1><p>Здесь мы делаем сайт типо Scetchfab.</p>")
    return render(request, 'gallery/about.html', context_data)