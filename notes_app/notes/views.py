from django.shortcuts import render
from django.http import HttpResponse
from .models import Notes, Categories


def index(request):
    return HttpResponse("Hello from Notes app")

def notes(request):
    notes = Notes.objects.select_related('categories').all()
    return render(request, 'notes/index.html', {'data': notes})