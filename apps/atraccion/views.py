from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Atraccion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def lista(request):
	atracciones = Atraccion.objects.all().filter(estado= True)

	paginator = Paginator(atracciones, 1)
	page = request.GET.get('page')

	try:
			context = paginator.page(page)
	except PageNotAnInteger:
			context = paginator.page(1)
	except EmptyPage:
			context = paginator.page(paginator.num_pages)

	contexto = {'atracciones': atracciones, 'context': context}
	return render(request, 'atraccion/lista.html', contexto)

class Lista(ListView):
	model = Atraccion
	template_name = 'atraccion/lista.html'
	paginate_by = 1