from django.contrib import admin
from . models import Paciente
from . models import Doctor
from . models import Historial



# Register your models here.
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Historial)
