from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Atraccion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy
from .forms import CrearForm


class Lista(ListView):
    queryset = Atraccion.objects.all().filter(estado=True)
    template_name = 'atraccion/lista.html'
    paginate_by = 6


class Detalle(DetailView):
    model = Atraccion
    template_name = 'atraccion/detalle.html'


def Crear(request):
    if request.method == 'POST':
        form = CrearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atraccion:lista')
    form = CrearForm(instance=atraccion)  # creacionde el formulario

    # retorno a el formulario de html con el formulario creado
    return render(request, 'atraccion/crear.html', {'form': form})


def Editar(request, pk, template_name='atraccion/editar.html'):
    atraccion = get_object_or_404(Atraccion, pk=pk)
    form = CrearForm(request.POST or None, instance=atraccion)
    if form.is_valid():
        form.save()
        return redirect('atraccion:lista')
    return render(request, template_name, {'form': form})


def Eliminar(request, pk, template_name='atraccion/eliminar.html'):
    atraccion = get_object_or_404(Atraccion, pk=pk)
    if request.method == 'POST':
        atraccion.delete()
        return redirect('atraccion:lista')
    return render(request, template_name, {'object': atraccion})
