from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from cars.models import Car
from django.contrib import messages
from django.shortcuts import render, redirect
from cars.models import Events
from cars.models import Manufacturers




def cars(request):
    return HttpResponse("Hello world!")

def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')

def contact_us(request):
    if request.method == 'POST':
        # process form data
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact_us')
    return render(request, 'contact_us.html')

def booking(request):
    if request.method == 'POST':
        return redirect('booking')
    return render(request, 'booking.html')

def car_page(request):
   cars = Car.objects.all()
   return render(request, 'car_page.html', {'cars': cars})
  
  
   
def events(request):
 events = Events.objects.all()
 return render(request, 'events.html', {'events': events})

def hours(request):
     events = Events.objects.all()
     return render(request, 'hours.html', {'events': events})

def manufacturer(request):
    manufacturers = Manufacturers.objects.all()
    return render(request, 'manufacturer.html', {'manufacturers': manufacturers})


def ticket(request):
    if request.method == 'POST':
        return redirect('ticket')
    return render(request, 'ticket.html')
