from typing import Any
from django.db import models

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombreDelPaciente = models.CharField(max_length=100, verbose_name='Nombre del Paciente')
    dpi = models.CharField(max_length=20, verbose_name='DPI')
    fechaDeNacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    dirección = models.TextField(verbose_name='Dirección')
    recetaMedica = models.TextField(verbose_name='Receta Médica', null=True, blank=True)
    numeroTelefonico = models.CharField(max_length=15, verbose_name='Número Telefónico')
    fotoDelPaciente = models.ImageField(upload_to='imagenes/', verbose_name='Foto del Paciente', null=True)

    def __str__(self):
        fila = "Nombre del Paciente: " + self.nombreDelPaciente + " - " + "Fecha de Nacimiento: " + str(self.fechaDeNacimiento)
        return fila
    def delete(self, using=None, keep_parents=False):
        self.fotoDelPaciente.storage.delete(self.fotoDelPaciente.name)
        super().delete()

        
        

    


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Doctor')
    numeroColegiado = models.CharField(max_length=20, verbose_name='Número de Colegiado')
    especialidad = models.CharField(max_length=100, verbose_name='Especialidad')
    direccion = models.TextField(verbose_name='Dirección', null=True, blank=True)
    numeroTelefono = models.CharField(max_length=15, verbose_name='Número de Teléfono', null=True, blank=True)
    fotoDelDoctor = models.ImageField(upload_to='imagenes/', verbose_name='Foto del Doctor', null=True, blank=True)

    def __str__(self):
        fila = "Nombre del Doctor: " + self.nombre + " - " + "Especialidad: " + self.especialidad
        return fila
    def delete(self, using=None, keep_parents=False):
        self.fotoDelDoctor.storage.delete(self.fotoDelDoctor.name)
        super().delete()


class Historial(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name='Paciente', null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='Doctor', null=True)
    descripcion = models.TextField(verbose_name='Descripción')
    def __str__(self):
        return f'Historial {self.id} de {self.paciente} con el doctor {self.doctor}'


    

