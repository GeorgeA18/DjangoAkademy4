from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publicaciones

# Create your views here.

class HomePageView(ListView):
    template_name = "home.html"
    model = Publicaciones


class DetailPageView(DetailView):
    template_name = "post_detail.html"
    model = Publicaciones