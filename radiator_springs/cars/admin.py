from django.contrib import admin
from .models import Car
from .models import Events
from .models import Manufacturers

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(Car, CarAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name', 'event_detail')

admin.site.register(Events, EventAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer_name', 'manufacturer_description')

admin.site.register(Manufacturers, ManufacturerAdmin)