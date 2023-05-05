"""radiator_springs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cars import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('car_page', views.car_page, name='car_page'),
    path('events', views.events, name='events'),
    path('hours', views.hours, name='hours'),
    path('manufacturer', views.manufacturer, name='manufacturer'),
    path('ticket', views.ticket, name = 'ticket'),

    path('admin/', admin.site.urls),
]
