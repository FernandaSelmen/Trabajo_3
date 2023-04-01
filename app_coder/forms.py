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

    nombre_del_after = forms.CharField(max_length=30)
    tema_a_tocar = forms.CharField(max_length=200)
    hora_de_inicio= forms.TimeField()
    zoom = forms.URLField()
    

