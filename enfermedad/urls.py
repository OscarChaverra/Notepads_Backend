from django.urls import path
from . import views

urlpatterns = [
    path("add/",views.SaveDiseases.as_view(),name="saveDiseases"),
    path("ViewEnfermedad/",views.ViewEnfermedades.as_view(),name="ViewEnfermedad")
]
