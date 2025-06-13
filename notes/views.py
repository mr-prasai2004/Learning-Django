from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from . models import Notes
from .forms import NotesForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def add_like_view(request,pk):
   if request.method == 'POST':
    note=get_object_or_404(Notes, pk=pk) 
    note.likes += 1
    note.save()
    return HttpResponseRedirect(reverse('notes.detail', args=(pk,)))
   raise Http404


class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model=Notes
    success_url='/smart/notes'
    template_name= 'notes/notes_delete.html'
    login_url="/admin"


class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model=Notes
    success_url='/smart/notes'
    form_class = NotesForm
    login_url="/admin"


class NotesCreateView(LoginRequiredMixin,CreateView):
    model=Notes
    success_url='/smart/notes'
    form_class = NotesForm
    login_url="/admin"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user= self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin,ListView):
    model= Notes
    context_object_name="notes"
    template_name = "notes/notes_list.html"
    login_url="/admin"

    def get_queryset(self):
        return self.request.user.notes.all()

class PopularNotesListView(LoginRequiredMixin,ListView):
    model= Notes
    context_object_name="notes"
    template_name = "notes/notes_list.html"
    queryset = Notes.objects.filter(pk__gte=1)
    login_url="/admin"

# def list(request):
#     all_notes= Notes.objects.all()
#     return render(request,'notes/notes_list.html',{'notes':all_notes})


class NotesDetailView(LoginRequiredMixin,DetailView):
    model = Notes
    context_object_name= 'note'
    login_url="/admin"
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Notes Doesn't Exist")
#     return render(request, 'notes/notes_detail.html', {'note':note})
