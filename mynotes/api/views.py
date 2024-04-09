from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    
    
    return Response({"status" :200 ,  "message": "Get Routes", "payload" :routes})


@api_view(['GET'])
def getNotes(request):
    Note_obj = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(Note_obj , many = True)
    
    return Response( {"status" : 200 , "payload" : serializer.data})

@api_view(['GET'])
def getNote(request , id):
    Note_obj = Note.objects.get(id = id)
    serializer = NoteSerializer(Note_obj , many = False)
    
    return Response( {"status" : 200 , "payload" : serializer.data})

@api_view(['PUT'])
def updateNote(request , id):
    try:
        Note_obj =  Note.objects.get(id = id)
        serializer = NoteSerializer(Note_obj ,  data = request.data , partial = True)
    
        if not serializer.is_valid():
            return Response({"message" : "Something went wrong" , "errors" : serializer.errors})
        serializer.save()
        return Response({'payload' : serializer.data , 'message' : "You sent a Post request"})
    
    except Exception as e:
       return Response({"error" : "update Exception"})
   
@api_view(['DELETE'])
def deleteNote(request , id):
    try:
        Note.objects.get(id =id).delete()
        return Response({"message" : "note Deleted"})
    except Exception as e:
        return Response({"error" : "Delete Exception"})
    
@api_view(['PUT'])
def createNote(request):
    serializer = NoteSerializer(data=request.data) 
    if not serializer.is_valid():
        return Response({"message" : "Something went wrong" , "errors" : serializer.errors})  
    serializer.save()
    return Response({"message" : "Note Created"})