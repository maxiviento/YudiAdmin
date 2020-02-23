from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *


admin.site.register(Consulta)
admin.site.register(Programa)
admin.site.register(Origen)

class ChatA(admin.ModelAdmin):
    list_display = ('id', 'id_contacto_parseo_id')

admin.site.register(Parseo)
admin.site.register(Contacto_parseo)

admin.site.site_header = "Yudi admin"
