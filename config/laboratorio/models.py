from django.db import models


class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    # se agregan los campos ciudad y pais
    ciudad = models.CharField(max_length=255, default='Ciudad') 
    pais = models.CharField(max_length=255, default='Pais') 

    def __str__(self):
        return self.nombre
    

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE, related_name='director_general')
    # se agrega nuevo campo especialidad
    especialidad = models.CharField(max_length=255, default='Sin especialidad')

    def __str__(self):
        return f"{self.nombre} ({self.laboratorio.nombre})"
    

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='productos')
    f_fabricacion = models.DateField(help_text="La fecha debe ser desde el 2015")
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre
    

    def save(self, *args, **kwargs):
        # Validación para asegurarse de que la fecha es a partir de 2015
        if self.f_fabricacion.year < 2015:
            raise ValueError("La fecha de fabricación debe ser desde 2015 en adelante.")
        super().save(*args, **kwargs)