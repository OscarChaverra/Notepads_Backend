from django.urls import path
from . import views

urlpatterns = [
    path("deleteCalendar/",views.DeleteCalendar.as_view(),name="delete event"),
    path("calendarList/",views.CalendarList.as_view(),name="calendar list")
]
