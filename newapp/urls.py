
from . import views
from django.urls import path
urlpatterns = [
    path('newapp/',views.current_time, name = 'current_time')
]