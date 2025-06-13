from django.shortcuts import render
from django.http import Http404
from . models import Notes
from django.views.generic import ListView

class NotesListView(ListView):
    model= Notes
    context_context_name="notes"
    template_name = "notes/notes_list.html"

# Create your views here.


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Notes Doesn't Exist")
    return render(request, 'notes/notes_detail.html', {'note':note})
