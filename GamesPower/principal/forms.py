from dataclasses import fields
from pyexpat import model
from tkinter.ttk import Widget
from .models import Comunidad, Proveedores
from django.forms import ModelForm, ClearableFileInput


class formComunidad(ModelForm):
    class Meta:
        model= Comunidad
        fields= ['nombre', 'producto', 'mensaje']



class customClearableInput(ClearableFileInput):
    template_with_clear= '<br><label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class formArchivos(ModelForm):
    class Meta:
        model= Proveedores
        fields= ('nombre', 'mensaje', 'archivo')
        widgets= {
            'archivo': customClearableInput
        }
