from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить свой автомобиль', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contacts'},
        {'title': 'Войти', 'url_name': 'login'}]

posts = Cars.objects.all()
context = {
    'posts': posts,
    'menu': menu,
    'title': 'Гдавная страница'
}

def empty_list(request):
    return HttpResponse("Главная страница")

def index(request):
    return render(request,'cars/index.html', context=context)

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def about(request):
    return render(request,'cars/about.html', {'title': 'О сайте', 'menu': menu, 'posts': posts})

def add_page(request):
    return HttpResponse("Добавление статьи")

def contacts(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')