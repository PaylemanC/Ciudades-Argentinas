from django.shortcuts import render
from django.http import HttpResponse
# from .models import City
from .models import *

# Create your views here.
def index(request):
    # return HttpResponse('Hola mundo!')
    cities = City.objects.all()
    return render(request, 'cities.html', {'cities': cities})

def get_city(request, id):
    city = City.objects.get(id=id)
    # City.objects.filter(name='Córdoba Capital')
    return render(request, 'city.html', {'city': city})