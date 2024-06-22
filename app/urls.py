from django.urls import path
from .views import HomePageView, DetailPageView
from .views import UpdatePageView, CreatePageView

urlpatterns = [
    path("", HomePageView.as_view(),name= "home"),
    path("detail/<int:pk>",DetailPageView.as_view(), name = "detail"),
    path("create", CreatePageView.as_view(),name= "create"),
]