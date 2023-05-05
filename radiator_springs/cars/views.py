from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from cars.models import Car


def cars(request):
    return HttpResponse("Hello world!")

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def contact_us(request):
    template = loader.get_template('contact_us.html')
    return HttpResponse(template.render())

def booking(request):
    template = loader.get_template('booking.html')
    return HttpResponse(template.render())

def car_page(request):
   cars = Car.objects.all()
   return render(request, 'car_page.html', {'cars': cars})
  
  
   
def events(request):
    template = loader.get_template('events.html')
    return HttpResponse(template.render())

def hours(request):
    template = loader.get_template('hours.html')
    return HttpResponse(template.render())

def manufacturer(request):
    template = loader.get_template('manufacturer.html')
    return HttpResponse(template.render())




