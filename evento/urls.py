from django.urls import path
from . import views

urlpatterns = [
    path("events/<int:typeRice>/",views.Events.as_view(),name="events"),
    path("calendarEvents/",views.EventView.as_view(),name="events"),
    path("createSpecialEvent/",views.CreateSpecialEvent.as_view(),name="create special event"),
    # path("modifySpecialEvent/",views.ModifySpecialEvent.as_view(),name = "modify special event"),
    path("deleteSpecialEvent/",views.DeleteSpecialEvent.as_view(),name="delete special event") ,
    path("ModificarFecha",views.Update.as_view(),name='Modificar')   
]
