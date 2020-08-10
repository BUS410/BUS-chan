from math import ceil

from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Question

QUESTIONS_IN_ONE_PAGE = 20


def index(request):
    questions = Question.objects.order_by('-id')
    pages = ceil(len(questions) / QUESTIONS_IN_ONE_PAGE)
    questions = questions[:QUESTIONS_IN_ONE_PAGE]
    return render(request, 'forum/list.html', {'questions_list': questions,
                                               'pages': range(1, pages + 1)})


def forum(request, page):
    questions = Question.objects.order_by('-id')
    pages = ceil(len(questions) / QUESTIONS_IN_ONE_PAGE)
    questions = questions[(page - 1) * QUESTIONS_IN_ONE_PAGE:
                          page * QUESTIONS_IN_ONE_PAGE]
    for q in questions:
        q.body = q.body.split('\n\n')[0]
    return render(request, 'forum/list.html', {'questions_list': questions,
                                               'pages': range(1, pages + 1)})


def detail(request, q_id):
    try:
        q = Question.objects.get(id=q_id)
    except Exception as e:
        print(e)
        raise Http404('Вопрос не найден')

    answers_list = q.answer_set.order_by('-id')

    return render(request, 'forum/detail.html',
                  {
                      'question': q,
                      'answers': answers_list,
                  }
                  )


def leave_answer(request, q_id):
    try:
        q = Question.objects.get(id=q_id)
    except Exception as e:
        print(e)
        raise Http404('Вопрос не найден')

    q.answer_set.create(author=request.POST['author'][:50] if request.POST[
        'author'].strip() else 'noname',
                        body=request.POST['text'] if request.POST[
                            'text'].strip() else 'я не знаю ответ')

    return HttpResponseRedirect(reverse('detail', args=(q.id,)))


def leave_question(request):
    Question(
        author=request.POST['author'][:50] if request.POST[
            'author'].strip() else 'noname',
        body=request.POST['text'] if request.POST[
            'text'].strip() else 'Я решил(-а) не задавать вопрос.',
    ).save()
    return HttpResponseRedirect(reverse('forum'))


def new_question(request):
    return render(request, 'forum/new_question.html')
