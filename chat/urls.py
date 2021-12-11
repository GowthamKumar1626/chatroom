from django.urls import path
from chat.views import index, room

urlpatterns = [
    path("", index, name="index"),
    path("<str:chat_room>/", room, name="room"),
]