from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm

visita = 0

# Vista para listar todos los laboratorios
def laboratorio_list(request):    
    global visita
    laboratorios = Laboratorio.objects.all()
    visita += 1    
    return render(request, 'laboratorio/list.html', {
        'laboratorios': laboratorios, 
        'visita': visita })


# Vista para crear un nuevo laboratorio
def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:laboratorio_list')  # Redirige a la lista de laboratorios
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/form.html', {'form': form})


# Vista para editar un laboratorio existente
def laboratorio_update(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:laboratorio_list') 
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/form.html', {'form': form})



# Vista para eliminar un laboratorio
def laboratorio_delete(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio:laboratorio_list')  # Redirige a la lista de laboratorios
    return render(request, 'laboratorio/confirm_delete.html', {'laboratorio': laboratorio})