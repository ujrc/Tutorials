# Register your models here.
from django.contrib import admin

from .models import Room, Message


class RoomAdmin(admin.ModelAdmin):
    list_dispaly = ['name', 'label']
    prepopulated_fields = {'label': ('name',)}

admin.site.register(Room, RoomAdmin)
admin.site.register(Message)
