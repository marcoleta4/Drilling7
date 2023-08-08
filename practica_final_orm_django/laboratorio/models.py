from django.db import models

from django.db import models



class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)  # Asegúrate de tener esta línea
    pais = models.CharField(max_length=100)    # Asegúrate de tener esta línea

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, default='Sin especialidad')  # Agregar valor predeterminado

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(default='2015-01-01')
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)