from django.db import models


class Question(models.Model):
    author = models.CharField('Автор вопроса', max_length=50)
    body = models.TextField('Текст вопроса')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.body[:50]


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.CharField('Автор ответа', max_length=50)
    body = models.TextField('Текст ответа')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.body[:50]
