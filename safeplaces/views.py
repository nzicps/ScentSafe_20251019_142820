from django.shortcuts import render, redirect
from .models import SafePlace
from .forms import SafePlaceForm

def home(request):
    places = SafePlace.objects.all()
    form = SafePlaceForm()
    if request.method == 'POST':
        form = SafePlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'home.html', {'places': places, 'form': form})
