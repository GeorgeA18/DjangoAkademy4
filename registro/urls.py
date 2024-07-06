from django.urls import path, include
from .views import SingupView, FirstPage


urlpatterns = [
    path("account", include("django.contrib.auth.urls")),
    path("app", SingupView.as_view(), name="singup"),
    path("", FirstPage.as_view(), name="first_page"),

]