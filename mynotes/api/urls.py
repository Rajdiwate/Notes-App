from .views import *
from django.urls import path

urlpatterns = [
    path('' , getRoutes ),
    path('notes/' , getNotes),
    path('notes/create' , createNote),
    path('notes/<id>/update/' , updateNote),
    path('notes/<id>/delete/' , deleteNote),
    path('notes/<id>/' , getNote),
    
   
]