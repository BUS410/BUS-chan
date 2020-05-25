from os.path import splitext
from django.db import models


# Create your models here.

class Chat(models.Model):
    name = models.CharField('Имя чата', max_length=50)
    category = models.CharField('Категория чата', max_length=50)
    is_private = models.BooleanField('Приватный чат')
    date = models.DateField('Дата создания чата', auto_now_add=True)

    def __str__(self):
        return self.name


class Messege(models.Model):
    author = models.CharField('Ник', max_length=50)
    date = models.DateTimeField('Дата отправки', auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField('Текст сообщения')
    file = models.FileField('Файл сообщения', upload_to='user_files/',
                            null=True, blank=True)

    def __str__(self):
        return self.text

    @property
    def get_file_format(self):
        if not self.file:
            return None
        file_format = splitext(self.file.name)[1]
        if file_format in ['.png', '.jpg', '.jpeg', '.webp']:
            return 'image'
        elif file_format in ['.mp4']:
            return 'video'
        elif file_format in ['.mp3', '.wav', '.ogg']:
            return 'audio'
        else:
            return 'file'
