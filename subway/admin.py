from django.contrib import admin

# Register your models here.
from .models import Train, Line, Station

admin.site.register(Train)
admin.site.register(Line)
admin.site.register(Station)
