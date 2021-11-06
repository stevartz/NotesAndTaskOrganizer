from django import forms
from .models import Class, Note, Assignment

class ClassForm(forms.Form):
    course_abbr = forms.CharField(label='Course Abbreviation', max_length=100)
    course_num = forms.CharField(label='Course Number', max_length=100)

class NoteForm(forms.Form):
    note_name = forms.CharField(label='Note name', max_length=100)
    for_class = forms.CharField(label='Course Abbreviation', max_length=100)

class AssignmentForm(forms.Form):
    name = forms.CharField(max_length=500)
    due_date = forms.DateField()
    description = forms.CharField(max_length=500)
    for_class = forms.CharField(label='Course Abbreviation', max_length=100)
    # make actual checkbox in html?
    checkbox = forms.BooleanField()
    # change actual color in html?
    colorcode = forms.CharField(max_length=500)
