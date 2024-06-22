from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publicaiones

# Create your views here.

class HomePageView(ListView):
    template_name = "home.html"
    model = Publicaiones


class DetailPageView(DetailView):
    template_name = "post_detail.html"
    model = Publicaiones