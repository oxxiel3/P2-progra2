from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static 



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('Pacientes', views.pacientes, name='Pacientes'),
    path('Pacientes/crear', views.crear_pacientes, name='crear'),
    path('Pacientes/editar', views.editar_pacientes, name='editar'),
    path('Doctores', views.Doctores, name='Doctores'),
    path('Doctores/crear', views.crear_doctores, name='crearDoctores'),
    path('Doctores/editar', views.editar_doctores, name='editarDoctores'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('Pacientes/editar/<int:id>', views.editar_pacientes, name='editar'),
    path('editar/doctores/<int:id>', views.editar_doctores, name='editarDoctores'),
    path('eliminarD/<int:id>', views.eliminar_doctores, name='eliminarD'),
    path('Historial_Clinico', views.history, name='historial'),
    path('Historial_Clinico/crear', views.create_history, name='createHIstory'),
    path('Historial_Clinico/editar/<int:id>', views.editar_history, name='editHIstory'),
    path('Historial_Clinico/eliminar/<int:id>', views.eliminar_history, name='eliminarH'),
    
  

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
