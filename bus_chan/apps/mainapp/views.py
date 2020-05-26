from random import choice
from django.shortcuts import render
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from .models import Chat, Message

CATEGORIES = {
    'Металл и рок': 'metal_and_rock',
    'Реп и поп': 'rap_and_pop',
    'Классика': 'classic',
    'Nightcore': 'nightcore',
    'Программирование': 'programming',
    '2D графика': '2d',
    '3D графика': '3d',
    'Дизайн': 'design',
    'MMORPG': 'mmorpg',
    'RPG': 'rpg',
    'Экшон': 'action',
    'Визуальные новеллы': 'visual_novel',
    'Аниме': 'anime',
    'Джоджо': 'jojo',
    'Манга': 'manga',
    'Ранобэ': 'ranobe',
    'Другое': 'other',
}


def index(request):
    return render(request, 'mainapp/base.html')


def category(request, category_name):
    chats_category = None
    chats = Chat.objects.all().filter(is_private=False, category=category_name)
    for key, val in CATEGORIES.items():
        if val == category_name:
            chats_category = key
            break

    return render(request, 'mainapp/category.html',
                  {'chats': list(reversed(chats)),
                   'category': chats_category})


def newchat(request):
    return render(request, 'mainapp/newchat.html',
                  {'categories': CATEGORIES.keys()})


def create_newchat(request):
    name = request.POST['name']
    cat = CATEGORIES[request.POST['category']]
    is_private = bool(request.POST.get('private', ''))

    new_chat = Chat(name=name, category=cat, is_private=is_private)
    new_chat.save()

    return render(request, 'mainapp/detail_chat.html', {'chat_id': new_chat.id})


def chat(request, chat_id):
    try:
        current_chat = Chat.objects.get(id=chat_id)
    except Exception as e:
        print(e)
        raise Http404("Чат не найден")

    massages = current_chat.message_set.order_by('id')
    cat = current_chat.category
    for key, val in CATEGORIES.items():
        if val == cat:
            cat = key
            break

    return render(request, 'mainapp/chat.html',
                  {'chat': current_chat, 'massages': massages,
                   'category': cat})


def send_message(request, chat_id):
    Message(chat=Chat.objects.get(id=chat_id),
            text=request.POST['text'],
            author=request.POST['author']).save()

    return HttpResponseRedirect(reverse('chat', args=[chat_id]))


def random_chat(request):
    try:
        chats = Chat.objects.all().filter(is_private=False)
        return chat(request, choice(chats).id)
    except Exception as e:
        print(e)
        raise Http404('Чаты не найдены')
