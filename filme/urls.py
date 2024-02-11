
from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme


urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes/', Homefilmes.as_view()),
    path('filmes/<int:pk>', Detalhesfilme.as_view()),
]