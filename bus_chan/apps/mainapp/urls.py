from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('category/<category_name>/', views.category, name='category'),
    path('newchat/', views.newchat, name='newchat'),
    path('create_newchat/', views.create_newchat, name='create_newchat'),
    path('chat/<int:chat_id>/', views.chat, name='chat'),
    path('private_chat/<key>/', views.private_chat, name='private_chat'),
    path('chat/<int:chat_id>/send_messege/', views.send_message,
         name='send_message'),
    path('random/', views.random_chat, name='random_chat'),
    path('get_ticket/', views.get_ticket, name='ticket'),
)
