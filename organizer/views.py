from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.list import ListView
from .models import Assignment, Class, Note
from .forms import ClassForm, NoteForm, AssignmentForm

# Homepage
def homepage(request):
    return render(request, 'organizer/generic_template.html')

# add a class
def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            c = Class()
            c.course_abbr = form.cleaned_data['course_abbr']
            c.course_num = form.cleaned_data['course_num']
            c.save()
            return HttpResponseRedirect(reverse('organizer:assignments'))
        else:
            return HttpResponseRedirect(reverse('organizer:addclass'))
    form = ClassForm()
    return render(request, 'organizer/addclass.html', {'form': form})

# add a note file
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            n = Note()
            n.note_name = form.cleaned_data['note_name']
            n.for_class = form.cleaned_data['for_class']
            n.save()
            return HttpResponseRedirect(reverse('organizer:assignments'))
        else:
            return HttpResponseRedirect(reverse('organizer:addnote'))
    form = NoteForm()
    return render(request, 'organizer/addnote.html', {'form': form})

# add an assignment file
def add_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            a = Assignment()
            a.name = form.cleaned_data['name']
            a.due_date = form.cleaned_data['due_date']
            a.description = form.cleaned_data['description']
            a.for_class = form.cleaned_data['for_class']
            a.checkbox = form.cleaned_data['checkbox']
            a.colorcode = form.cleaned_data['colorcode']
            a.save()
            return HttpResponseRedirect(reverse('organizer:assignments'))
        else:
            return HttpResponseRedirect(reverse('organizer:addassignment'))
    form = AssignmentForm()
    return render(request, 'organizer/addassignment.html', {'form': form})


# view for assignments/notes page
class ClassView(generic.ListView):
    model = Class
    template_name = 'organizer/assignments.html'
    context_object_name = 'latest_class_list'
    qs = Class.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ClassView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
        context['assignments'] = Assignment.objects.all()
        return context

