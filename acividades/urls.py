from django.urls import path
from . import views

urlpatterns = [
    path("actividades/<int:tipoArroz>",views.activitysView.as_view(),name="activitys"),
    path("news/",views.NewsActivitys.as_view(),name="create new data")
]
