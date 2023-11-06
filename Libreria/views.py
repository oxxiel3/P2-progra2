from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Paciente
from . forms import PacienteForm
from .models import Doctor
from .forms import DoctorForm
from .models import Historial
from .forms import HistorialForm




def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')



def pacientes(request):
    pacientes = Paciente.objects.all()
   
    return render(request, 'Pacientes/index.html', {'Pacientes': pacientes})

def crear_pacientes(request):
    formulario = PacienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Pacientes')
    return render(request, 'Pacientes/crear.html', {'formulario': formulario})

def editar_pacientes(request, id):
    paciente = Paciente.objects.get(id=id)
    formulario = PacienteForm(request.POST or None, request.FILES or None, instance=paciente)
    if formulario.is_valid() and request.POST:
        formulario.save()
    return render(request, 'Pacientes/editar.html', {'formulario': formulario})

def eliminar(request, id):
    pacientes = Paciente.objects.get(id=id)
    pacientes.delete()
    return redirect('Pacientes')





def Doctores(request):
    doctores=Doctor.objects.all()

    return render(request, 'Doctores/index.html', {'doctores':doctores})

def crear_doctores(request):
    formulario = DoctorForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Doctores')
    return render(request, 'Doctores/crear.html', {'formulario':formulario})

def editar_doctores(request, id):
    doctores=Doctor.objects.get(id=id)
    formulario = DoctorForm(request.POST or None, request.FILES or None, instance=doctores)
    if formulario.is_valid() and request.POST:
        formulario.save()
    return render(request, 'Doctores/editar.html', {'formulario': formulario})

def eliminar_doctores(request, id):
    doctores = Doctor.objects.get(id=id)
    doctores.delete()
    return redirect('Doctores')
   


        

def history(request):
    histories=Historial.objects.all()

    return render(request, 'Historial_Clinico/index.html', {'historiales':histories})

def create_history(request):
    
    form = HistorialForm(request.POST)
    
    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
        
            cleaned_data['paciente_id'] = request.POST.get('paciente_id')
            cleaned_data['doctor_id'] = request.POST.get('doctor_id')
            cleaned_data['descripcion'] = request.POST.get('descripcion')

            form.cleaned_data = cleaned_data
            history = form.save(commit=False)
            history.paciente_id = request.POST.get('paciente_id')
            history.doctor_id = request.POST.get('doctor_id')
            history.descripcion = request.POST.get('descripcion')

            history.save()

        else:
           print (form.errors)
    return render(request, 'historial_clinico/crear.html', {'formulario': form})


def editar_history(request, id):
    histories=Historial.objects.get(id=id)
    print(histories)
    
    formulario = HistorialForm(request.POST or None, instance=histories, initial={'paciente': histories.paciente})
    if formulario.is_valid() and request.POST:
        formulario.save()
    return render(request, 'Historial_Clinico/editar.html', {'formulario': formulario})

def eliminar_history(request, id):
    histories=Historial.objects.get(id=id)
    histories.delete()
    return redirect('historial')












    


# Create your views here.
