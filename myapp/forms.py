from django import forms 


class resultados(forms.Form):
    array = forms.CharField(label="Inserte la lista", required=True)