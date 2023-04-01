from django import forms


class ProfesorForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    correo = forms.EmailField()
    profesion = forms.CharField(max_length=30)
    
class AlumnoForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    correo = forms.EmailField()
   
class BuscarPrefesor(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    

class EntregablesForm(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=20)
    proyecto = forms.CharField(max_length=60)
    hora = forms.TimeField()

class AfterForm(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    tema = forms.CharField(max_length=20)
    hora = forms.TimeField()
    zoom = forms.URLField()
   