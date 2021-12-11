from django.urls import path
from chat.views import index, room

urlpatterns = [
    path("", index, name="index"),
    path("<str:room_name>/", room, name="room"),
]