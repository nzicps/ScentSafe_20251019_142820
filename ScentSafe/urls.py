from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.redirect_root),
    path('map/', include('maps.urls')),
    path('map/', views.map_view, name='map'),
    path('add_place/', views.add_place, name='add_place'),
]

