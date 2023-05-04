from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(Car, CarAdmin)
