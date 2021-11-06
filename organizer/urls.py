from django.urls import path
from . import views

app_name = 'organizer'
urlpatterns = [
    path('home', views.homepage, name='index'),
    path('assignments', views.ClassView.as_view(), name='assignments'),
    path('addclass', views.add_class, name='addclass'),
    path('addnote', views.add_note, name='addnote'),
    path('addassignment', views.add_assignment, name='addassignment'),
]
