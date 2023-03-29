from django import forms


class ProfesorForm(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    correo = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    