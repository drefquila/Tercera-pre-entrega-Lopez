from django import forms

class formulario(forms.Form):
    categorias=((1,'maquinaria'),
                (2,'implementos'),
                (3,'suplementos'))
    tipo=forms.ChoiceField(label='tipo de objeto:',choices=categorias,required=True)
    nombre=forms.CharField(label='nombre del objeto:',max_length=30,required=True)
    precio=forms.IntegerField(label='precio del objeto:',required=True)

class Buscarobjeto(forms.Form):
    categorias=((1,'maquinaria'),
                (2,'implementos'),
                (3,'suplementos'))
    tipo=forms.ChoiceField(label='tipo de objeto',choices=categorias,required=True)
    nombre=forms.CharField(label='nombre del objeto',max_length=30,required=True)
