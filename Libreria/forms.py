from django import forms
from .models import Paciente, Doctor, Historial


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class HistorialForm(forms.ModelForm):

    paciente_id = forms.ModelChoiceField(queryset=Paciente.objects.all(), label='Paciente', widget=forms.Select(attrs={'name': 'paciente_id', 'id': 'paciente_id'}))
    doctor_id = forms.ModelChoiceField(queryset=Doctor.objects.all(), label='Doctor', widget=forms.Select(attrs={'name': 'doctor_id', 'id': 'doctor_id'}))

    class Meta:
        model = Historial
        fields = ['descripcion']



