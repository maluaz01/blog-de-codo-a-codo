from django import forms
from django.forms import ValidationError


class ContenidoForm(forms.Form):

    TIPO_CONTENIDO = (
        ('','-Seleccione-'),
        (1,'Chiste'),
        (2,'Cuento'),
        (3,'Poesia'),
    )

    categoria = forms.ChoiceField(
        label='Categoria',
        choices=TIPO_CONTENIDO,
        initial='',
        widget=forms.Select(attrs={'class':'form-control'})
    )

    autor = forms.CharField(
            label='Autor',
            required=True,
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el autor'})
            )

    titulo = forms.CharField(
            label='Titulo',
            required=True,
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el titulo'})
            )

    contenido = forms.CharField(
            label='Contenido',
            max_length=1000,
            widget= forms.Textarea(attrs={'class':'form-control'})
        )


    
    def clean_mensaje(self):
        data = self.cleaned_data['Contenido']
        if len(data) < 10:
            raise ValidationError("El contenido es muy corto")
        return data
    