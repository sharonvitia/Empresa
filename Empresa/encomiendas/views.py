from django.shortcuts import render, redirect
from .models import Encomienda
from .forms import EncomiendaForm

def index(request):
    return render(request, 'encomiendas/index.html')

def listar_encomiendas(request):
    encomiendas = Encomienda.objects.all()
    return render(request, 'encomiendas/listar.html', {'encomiendas': encomiendas})

def nueva_encomienda(request):
    if request.method == 'POST':
        form = EncomiendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_encomiendas')
    else:
        form = EncomiendaForm()
    return render(request, 'encomiendas/nueva.html', {'form': form})
