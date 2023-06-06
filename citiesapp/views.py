from django.shortcuts import render
from django.http import HttpResponse
# from .models import City
from .models import *

# Create your views here.
def index(request):
    cities = City.objects.all()
    # City.objects.get(id=2) 
    # City.objects.filter(name='Córdoba Capital')

    # return HttpResponse('Hola mundo!')
    return render(request, 'cities.html')