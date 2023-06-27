from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes, name='notes'),
    path('create/', views.create_note, name='create'),
    path('<int:note_id>/delete/', views.delete_note, name='delete'),
    path('<int:note_id>/correct/', views.correct_note, name='correct'),
]
