from django.http import JsonResponse
from django.shortcuts import render
from .models import Train
from .models import Line
from .models import Station

# Create your views here.
def lines_list(request):
    lines = Line.objects.values()
    return JsonResponse({'lines': list(lines)}, safe=False)

def stations_list(request):
    stations = Station.objects.values()
    return JsonResponse({'stations': list(stations)}, safe=False)

def train_list(request):
    trains = Train.objects.values()
    return JsonResponse({'trains': list(trains)}, safe=False)
