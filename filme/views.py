from typing import Any
from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


class Homepage(TemplateView):
    template_name = "homepage.html"
    

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    
''' 
    #apagar se não funcionar
    context_object_name = 'filmes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filmes_comedia'] = Filme.objects.filter(categoria='Comédia')
        return context
'''

    
class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    
    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        return super().get(request, *args, **kwargs) 
        
    
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:10]
        context["filmes_relacionados"] = filmes_relacionados
        return context
        