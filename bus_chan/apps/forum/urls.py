from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name='forum'),
    path('page=<int:page>', views.forum, name='page'),
    path('q:<int:q_id>', views.detail, name='detail'),
    path('new_question', views.new_question, name='new_question'),
    path('leave_question', views.leave_question, name='leave_question'),
    path('q:<q_id>/leave_asnwer', views.leave_answer, name='leave_answer'),
)
