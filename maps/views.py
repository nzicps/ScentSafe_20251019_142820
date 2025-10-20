from django.shortcuts import render
from django.conf import settings

def map_view(request):
    return render(request, 'maps/map.html', {'google_api_key': getattr(settings, 'GOOGLE_MAPS_API_KEY', '')})
