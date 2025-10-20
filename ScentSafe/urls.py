from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map'),
    path('add_place/', views.add_place, name='add_place'),
]
