from django.shortcuts import render
from django.http import JsonResponse
# rest api imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializer import TaskSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-created')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)