from django.urls import path
from . import views

urlpatterns = [
    path("add/",views.SavePlagues.as_view(),name="saveDisease"),
    
]
