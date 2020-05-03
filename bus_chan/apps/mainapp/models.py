from django.db import models

# Create your models here.

class Chat(models.Model):
	CATEGORYES = [
	    ('metal_and_rock', 'Металл и рок'),
	    ('rap_and_pop', 'Реп и поп'),
	    ('classic', 'Классика'),
	    ('nightcore', 'Nightcore'),
	    ('programming', 'Программирование'),
	    ('2d', '2D графика'),
	    ('3d', '3D графика'),
	    ('design', 'Дизайн'),
	    ('mmorpg', 'MMORPG'),
	    ('rpg', 'RPG'),
	    ('action', 'Экшон'),
	    ('visual_novel', 'Визуальные новеллы'),
	    ('anime', 'Аниме'),
	    ('jojo', 'Джоджо'),
	    ('manga', 'Манга'),
	    ('ranobe', 'Ранобэ'),
	    ('other', 'Другое'),
	]
	name = models.CharField('Имя чата', max_length = 50)
	category = models.CharField('Категория чата', max_length = 50,
				choices=CATEGORYES, default='Freshman')
	is_private = models.BooleanField('Приватный чат')
	date = models.DateField('Дата создания чата', auto_now_add=True)

	def __str__(self):
		return self.name

class Messege(models.Model):
	author = models.CharField('Ник', max_length=50)
	date = models.DateTimeField('Дата отправки', auto_now_add=True)
	chat = models.ForeignKey(Chat, on_delete = models.CASCADE)
	text = models.TextField('Текст сообщения')
	image = models.ImageField('Картинка сообщения', upload_to='user_images/',
								null=True, blank=True)

	def __str__(self):
		return self.text

