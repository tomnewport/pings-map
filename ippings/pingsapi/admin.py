from django.contrib import admin
from .models import Location, Ping, Country

# Register models here.
admin.site.register(Location)
admin.site.register(Ping)
admin.site.register(Country)