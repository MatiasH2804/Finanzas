from django.db import models
from django.contrib.auth.models import User

class Ingreso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.descripcion} - {self.cantidad}"

class Gasto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.descripcion} - {self.cantidad}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Configuracion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    moneda = models.CharField(max_length=10, default="USD")

    def __str__(self):
        return f"Configuración de {self.usuario.username}"
