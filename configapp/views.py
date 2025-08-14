from django.shortcuts import render
from django.db.models import Q
from .models import rooms, users, deal, employee, room_type, room_size
from configapp.models import *

from django.shortcuts import render
from configapp.models import rooms, users, deal

def index(request):
    return render(request, 'index.html')

def room_list(request):
    all_rooms = rooms.objects.all()
    return render(request, 'room_list.html', {'rooms': all_rooms})

def users_list(request):
    all_users = users.objects.all()
    return render(request, 'users_list.html', {'users': all_users})

def deal_list(request):
    all_deals = deal.objects.all()
    return render(request, 'deal_list.html', {'deals': all_deals})


def global_search(request):
    query = request.GET.get('search', '')

    # Default qiymatlar — hammasi bo‘sh queryset
    rooms_list = rooms.objects.none()
    users_list = users.objects.none()
    deals_list = deal.objects.none()
    employees_list = employee.objects.none()
    room_types_list = room_type.objects.none()
    room_sizes_list = room_size.objects.none()

    if query:
        # Rooms bo‘yicha qidiruv
        rooms_list = rooms.objects.filter(
            Q(title__icontains=query) |
            Q(id_room_type__title__icontains=query) |
            Q(id_room_size__title__icontains=query) |
            Q(id_employee__name__icontains=query) |
            Q(id_employee__surname__icontains=query)
        )

        # Users bo‘yicha qidiruv
        users_list = users.objects.filter(
            Q(name__icontains=query) |
            Q(surname__icontains=query) |
            Q(phone__icontains=query)
        )

        # Deals bo‘yicha qidiruv
        deals_list = deal.objects.filter(
            Q(id_user__name__icontains=query) |
            Q(id_room__title__icontains=query)
        )

        # Employee bo‘yicha qidiruv
        employees_list = employee.objects.filter(
            Q(name__icontains=query) |
            Q(surname__icontains=query) |
            Q(email__icontains=query)
        )

        # Room Type bo‘yicha qidiruv
        room_types_list = room_type.objects.filter(
            Q(title__icontains=query)
        )

        # Room Size bo‘yicha qidiruv
        room_sizes_list = room_size.objects.filter(
            Q(title__icontains=query) |
            Q(discription__icontains=query)
        )

    return render(request, 'index.html', {
        'query': query,
        'rooms': rooms_list,
        'users': users_list,
        'deals': deals_list,
        'employees': employees_list,
        'room_types': room_types_list,
        'room_sizes': room_sizes_list,
    })