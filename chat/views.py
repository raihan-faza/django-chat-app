from django.shortcuts import render
from models import *
# Create your views here.


def index(request):
    rooms = Room.objects.all()
    return render(request, 'index/html', {'rooms':rooms})

def chat_room(request,slug):
    room = Room.objects.get(slug=slug)
    return render(request,'room.html', {'room':room})

def create_room(request):
    return