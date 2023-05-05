from django.contrib import admin
from .models import Car
from .models import Events

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(Car, CarAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name', 'event_detail')

admin.site.register(Events, EventAdmin)

