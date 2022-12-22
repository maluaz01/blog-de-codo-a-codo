from django import forms
from .models import Post

class Formulario_Admin(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'texto',)
