from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Evento
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def cargar_inicio(request):
    return render(request, "EventViewApp/inicio.html")
    
class EventoList(ListView):
    model = Evento
    template_name = 'EventViewApp/lista_eventos.html'


class EventoCreate(LoginRequiredMixin,CreateView):
    model = Evento
    fields = ['nombre','descripcion','empresa','fecha']
    template_name = 'EventViewApp/nuevo_evento.html'
    success_url = reverse_lazy('lista_eventos')






































































































































from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class RegistroUsuario(CreateView):
    model = Evento   
    form_class = UserCreationForm
    template_name = "EventViewApp/registrar.html"
    success_url = reverse_lazy('inicio')

