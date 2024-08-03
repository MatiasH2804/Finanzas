from django import forms

class SueldoFormulario(forms.Form):
    monto = forms.DecimalField(max_digits=10, decimal_places=2)

class GastoFormulario(forms.Form):
    categoria = forms.CharField()
    monto = forms.DecimalField(max_digits=10, decimal_places=2)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)

class CategoriaFormulario(forms.Form):
    nombre = forms.CharField()

class IngresoFormulario(forms.Form):
    cantidad = forms.DecimalField(max_digits=10, decimal_places=2)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)

class BuscarTransaccionForm(forms.Form):
    transaccion = forms.CharField()
