from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from cars.models import Car
from django.contrib import messages
from django.shortcuts import render, redirect
from cars.models import Events




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
    template = loader.get_template('hours.html')
    return HttpResponse(template.render())

def manufacturer(request):
    template = loader.get_template('manufacturer.html')
    return HttpResponse(template.render())


def ticket(request):
    template = loader.get_template('ticket.html')
    return HttpResponse(template.render())

