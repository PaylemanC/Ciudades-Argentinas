from django.contrib import admin
# from .models import City
from .models import *

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'population', 'province', 'created_date', 'published_date')

admin.site.register(City, CityAdmin)