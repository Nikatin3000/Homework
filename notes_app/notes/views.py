from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Notes, Categories
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import NotesForm


# def index(request):
#     return HttpResponse("Hello from Notes app")

def notes(request):
    notes = Notes.objects.select_related('categories').all()
    return render(request, 'notes/index.html', {'data': notes})

def create_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            # form.save()
            q = Notes(categories=form.cleaned_data['categories'], title=form.cleaned_data['title'],
                         text=form.cleaned_data['text'], reminder=form.cleaned_data['reminder'])
            q.save()

            return HttpResponseRedirect('/notes/')
    else:
        form = NotesForm()

    return render(request, 'notes/create_note.html', {'form': form})


def delete_note(request, note_id):
        if request.method == 'POST':
            note = Notes.objects.get(pk=note_id)
            note.delete()
            return redirect('/notes/')
        else:
            return HttpResponseRedirect('/notes/')


def correct_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/notes/')
    else:
        form = NotesForm(instance=note)

    return render(request, 'notes/correct_note.html', {'form': form})