from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Publicaciones
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    template_name = "home.html"
    model = Publicaciones


class DetailPageView(DetailView):
    template_name = "post_detail.html"
    model = Publicaciones



# Para editar
class UpdatePageView(UpdateView):
    template_name = "post_update.html"
    model = Publicaciones
    fields = [
        "titulo", "descripcion"
    ]
    success_url = reverse_lazy("home")

class CreatePageView(CreateView):
    template_name = "post_create.html"
    model = Publicaciones
    fields = ["titulo","descripcion"]
    success_url = reverse_lazy("home")

class DeleteView(DeleteView):
    template_name = "post_delete.html"
    model = Publicaciones
    success_url = reverse_lazy("home")
