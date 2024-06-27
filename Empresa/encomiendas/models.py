from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    
    app_label='encomiendas'

    def __str__(self):
        return self.nombre

class Encomienda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    entregado = models.BooleanField(default=False)

    app_label='encomiendas'
    
    def __str__(self):
        return f"{self.descripcion} - {self.cliente.nombre}"
