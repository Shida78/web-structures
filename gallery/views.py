from django.shortcuts import render
from django.http import HttpResponse

# request — это "письмо" от браузера с данными о пользователе
def home(request):
    # Мы пока не используем HTML-шаблоны, просто вернем строку.
    return HttpResponse("<h1>Добро пожаловать в 3D Хранилище</h1><p>Система работает.</p>")

def about(request):
    # Мы пока не используем HTML-шаблоны, просто вернем строку.
    return HttpResponse("<h1>Курс Web Структуры</h1><p>Здесь мы делаем сайт типо Scetchfab.</p>")
