from django.urls import path
from .views import HomePageView, DetailPageView

urlpatterns = [
    path("", HomePageView.as_view(),name= "home"),
    path("detail/<int:pk>",DetailPageView.as_view(), name = "detail")
]