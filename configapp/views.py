from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    all_rooms = rooms.objects.all()
    employees = employee.objects.all()
    user = users.objects.all()
    deals = deal.objects.all()
    context = {
        "room_list": all_rooms,
        "employees": employees,
        "user": user,
        "deal": deals,
        "title": "NEW TITLE"
    }
    return render(request, 'index.html', context=context)


def room_list(request):
    all_rooms = rooms.objects.all()
    return render(request, 'room_list.html', {"rooms": all_rooms})

def add_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', context={"form": form})

def update_room(request, pk):
    room = get_object_or_404(rooms, pk=pk)
    form = RoomForm(request.POST or None , instance=room)
    if form.is_valid():
        form.save()
        return redirect('update_room')
    return render(request, 'update_room.html', {"form": form})

def del_room(request, pk):
    room = get_object_or_404(rooms, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'index.html', {"room": room})

def deal_room_view(request):
    deal_room = rooms.objects.all()
    deals = deal.objects.all()
    return render(request, 'deal_list.html', {'deal_room': deal_room, 'deals': deals})



def add_deal(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deal_list')
    else:
        form = DealForm()
    return render(request, 'deal_form.html', {'form': form})
