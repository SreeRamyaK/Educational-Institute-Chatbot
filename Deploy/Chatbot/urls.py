from django.urls import path
from Chatbot import views

urlpatterns = [
    path('', views.index,name='index'),
    path('chatbot/', views.chatbot_response_view,name='chatbot'),
]