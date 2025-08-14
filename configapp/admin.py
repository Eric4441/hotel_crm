from django.contrib import admin

from .models import room_type, room_size, employee, rooms, users, deal

admin.site.register(room_type)
admin.site.register(room_size)
admin.site.register(employee)
admin.site.register(rooms)
admin.site.register(users)
admin.site.register(deal)

# Register your models here.
