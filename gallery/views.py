from django.shortcuts import render
#from django.http import HttpResponse

# request — это "письмо" от браузера с данными о пользователе
def home(request):
    # Имитация данных из базы (список словарей)
    fake_database = [
    {'id': 1, 'name': 'Sci-Fi Helmet', 'file_size': '15 MB'},
    {'id': 2, 'name': 'Old Chair', 'file_size': '2 MB'},
    {'id': 3, 'name': 'Cyber Truck', 'file_size': '10 MB'},
    {'id': 4, 'name': 'Smartphone', 'file_size': '12 MB'},
    ]
    # Это словарь Python.
    # Ключи словаря станут именами переменных в HTML.
    context_data = {
    'page_title': 'Главная Галерея',
    #'models_count': 0, # Попробуйте поменять на 5, чтобы проверить условие
    'assets': fake_database, # Передаем весь список
    }

    # 2. Рендерим (смешиваем HTML и данные)
    # Путь указываем относительно папки templates: 'gallery/index.html'
    return render(request, 'gallery/index.html', context_data)

def about(request):
    context_data = {
    #'page_title': 'О нас',
    }
    # Мы пока не используем HTML-шаблоны, просто вернем строку.
    #return HttpResponse("<h1>Курс Web Структуры</h1><p>Здесь мы делаем сайт типо Scetchfab.</p>")
    return render(request, 'gallery/about.html', context_data)