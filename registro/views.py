from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.
class SingupView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/singup.html"
    success_url = reverse_lazy("login")  # Retorna a otra pagina, si no se coloca de error.


class FirstPage(TemplateView):
    template_name = "registration/first_page.html"


class LogoutPageView(TemplateView):
    template_name = "registration/logout.html"