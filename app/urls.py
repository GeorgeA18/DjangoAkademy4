from django.urls import path
from .views import HomePageView, DetailPageView, UpdatePageView, CreatePageView

urlpatterns = [
    path("", HomePageView.as_view(),name= "home"),
    path("detail/<int:pk>",DetailPageView.as_view(), name = "detail"),
    path("create", CreatePageView.as_view(),name= "create"),
    path("detail/<int:pk>/update",UpdatePageView.as_view(),name="update" ),
]