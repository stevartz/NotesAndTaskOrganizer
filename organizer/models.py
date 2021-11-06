from django.db import models
from django.forms import ModelForm
from django.utils import timezone

# Class
class Class(models.Model):
    course_abbr = models.CharField(max_length=100, default='')
    course_num = models.CharField(max_length=100, default='')


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['course_abbr', 'course_num']

# Assignment
class Assignment(models.Model):
    name = models.CharField(max_length=500, default='')
    due_date = models.DateField(default='')
    description = models.CharField(max_length=500, default='')
    for_class = models.CharField(max_length=100, default='')
    # make actual checkbox in html?
    checkbox = models.BooleanField(default=False)
    # change actual color in html?
    colorcode = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name + " due on " + str(self.due_date) + "for" + str(self.for_class)


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['name', 'due_date', 'description', 'checkbox', 'colorcode', 'for_class']

# Note
class Note(models.Model):
    note_name = models.CharField(max_length=100, default='')
    for_class = models.CharField(max_length=100, default='')
 

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['note_name', 'for_class']