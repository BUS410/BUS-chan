from django.contrib import admin
from .models import Message, Chat

# Register your models here.

admin.site.register(Chat)
admin.site.register(Message)
