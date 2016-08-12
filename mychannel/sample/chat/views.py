# Create your views here.
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Room, Message, gen_word


class ChatView(TemplateView):
    """docstring for ChatView"""
    template_name = 'chat/chat-home.html'


def new_room(request):
    """
    Randomly create a new room, and redirect to it.
    """
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = gen_word()
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
    return redirect(chat_room, label=label)


def chat_room(request, label):
        # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)
    # We want to show the last 50 messages, ordered most-recent-las
    template_name = 'chat/room.html'
    messages = reversed(room.messages.order_by('-timestamp')[:50])
    return render(request, template_name,
                  {'room': room,
                   'messages': messages,
                   })
