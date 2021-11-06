from django.contrib import admin
from .models import Class, Assignment, Note
# Register your models here.

class ClassAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['course_abbr']}),
        (None, {'fields': ['course_num']}),
    ]
    list_display = ('course_abbr', 'course_num')
    list_filter = ['course_num']
    search_fields = ['course_abbr']

class NoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['note_name']}),
        (None, {'fields': ['for_class']}),
    ]
    list_display = ('note_name', 'for_class')
    list_filter = ['note_name', 'for_class']
    search_fields = ['note_name', 'for_class']

class AssignmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['due_date']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['checkbox']}),
        (None, {'fields': ['colorcode']}),
        (None, {'fields': ['for_class']}),
    ]
    list_display = ('name', 'due_date', 'description', 'checkbox', 'colorcode', 'for_class')
    list_filter = ['name', 'due_date', 'description', 'checkbox', 'colorcode', 'for_class']
    search_fields = ['name', 'due_date', 'description', 'checkbox', 'colorcode', 'for_class']


admin.site.register(Class, ClassAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Assignment, AssignmentAdmin)