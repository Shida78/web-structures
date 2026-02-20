from django.shortcuts import render, redirect # Добавляем redirect
from .models import Asset
from .forms import AssetForm # Импортируем нашу новую форму

def upload(request):
    if request.method == 'POST':
        # Сценарий: Пользователь нажал "Отправить"
        # ВАЖНО: Передаем request.FILES, иначе файл потеряется!
        form = AssetForm(request.POST, request.FILES)

        if form.is_valid():
            # Если все поля заполнены верно - сохраняем в БД
            form.save()
            # И перекидываем пользователя на главную
            return redirect('home')
    else:
        # Сценарий: Пользователь просто зашел на страницу (GET)
        form = AssetForm() # Создаем пустую форму

    # Отдаем шаблон, передавая туда форму (заполненную ошибками или пустую)
    return render(request, 'gallery/upload.html', {'form': form})

# request — это "письмо" от браузера с данными о пользователе
def home(request):
   # ORM Запрос: "Дай мне все объекты Asset из базы"
   # order_by('-created_at') сортирует по полю created_at.
    # Минус (-) означает "по убыванию" (DESC).
    assets = Asset.objects.all().order_by('-created_at')
    #assets = Asset.objects.all()

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