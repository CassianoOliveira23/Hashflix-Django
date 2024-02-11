from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


class Homepage(TemplateView):
    template_name = "homepage.html"
    

class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Filme
    
class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Filme