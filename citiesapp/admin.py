from django.contrib import admin
# from .models import City
from .models import *

# Register your models here.
class CityAdmin(admin.ModelAdmin):
    list_display = list([field.name for field in City._meta.get_fields()]) # Llama a cada campo y lo transforma.

admin.site.register(City, CityAdmin)