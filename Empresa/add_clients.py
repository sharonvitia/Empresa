import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_empresa.settings')
django.setup()

from encomiendas.models import Cliente

clientes = [
    {'nombre': 'Cliente 1', 'email': 'cliente1@example.com'},
    {'nombre': 'Cliente 2', 'email': 'cliente2@example.com'},
    {'nombre': 'Cliente 3', 'email': 'cliente3@example.com'},
]

for cliente_data in clientes:
    cliente, created = Cliente.objects.get_or_create(**cliente_data)
    if created:
        print(f"Cliente {cliente.nombre} creado.")
    else:
        print(f"Cliente {cliente.nombre} ya existe.")
