from django.shortcuts import render
from django.http import JsonResponse
from .models import Place
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

def map_view(request):
    places = Place.objects.all()
    return render(request, 'map.html', {'places': places, 'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY})

@csrf_exempt
def add_place(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        lat = data.get('latitude')
        lng = data.get('longitude')
        description = data.get('description', '')
        place = Place.objects.create(name=name, latitude=lat, longitude=lng, description=description)
        return JsonResponse({'status': 'success', 'id': place.id})
    return JsonResponse({'status': 'error'}, status=400)
