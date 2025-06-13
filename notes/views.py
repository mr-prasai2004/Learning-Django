from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from . models import Notes
from .forms import NotesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
def add_like_view(request,pk):
   if request.method == 'POST':
    note=get_object_or_404(Notes, pk=pk) 
    note.likes += 1
    note.save()
    return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
   raise Http404

class NotesDeleteView(DeleteView):
    model=Notes
    success_url='/smart/notes'
    template_name= 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model=Notes
    success_url='/smart/notes'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model=Notes
    success_url='/smart/notes'
    form_class = NotesForm

class NotesListView(ListView):
    model= Notes
    context_object_name="notes"
    template_name = "notes/notes_list.html"

class PopularNotesListView(ListView):
    model= Notes
    context_object_name="notes"
    template_name = "notes/notes_list.html"
    queryset = Notes.objects.filter(pk__gte=1)

# def list(request):
#     all_notes= Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name= 'note'
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Notes Doesn't Exist")
#     return render(request, 'notes/notes_detail.html', {'note':note})
