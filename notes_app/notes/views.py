from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello from Notes app")

def notes(request):
    notes_list = ['note_1', 'note_2', 'note_3', 'note_4', 'note_5']
    context = {'notes_list': notes_list}
    return render(request, 'notes/index.html', context)