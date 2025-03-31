from django.urls import path
from . import views

urlpatterns = [
    path("add/",views.SavePlagues.as_view(),name="saveDisease"),
    path("ViewPlaga/",views.ViewPlaga.as_view(),name="ViewPlaga"),
]
