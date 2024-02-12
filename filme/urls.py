
from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme, Pesquisa_filme

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', Pesquisa_filme.as_view(), name='pesquisafilme'),
]