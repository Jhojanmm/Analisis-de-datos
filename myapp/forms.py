from django import forms 


class resultados(forms.Form):
    array = forms.CharField(label="Inserte la lista", required=False)
    file = forms.FileField(label="Anexe archivo", required=False)