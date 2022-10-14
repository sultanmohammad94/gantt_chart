from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task, Link
from .serializers import TaskSerializer, LinkSerializer


def index(request):
    return render(request, "core/index.html")

@api_view(['GET'])
def data_list(request, offset):
    is_get_request = True if request.method == "GET" else False
    
    if is_get_request:
        tasks = Task.objects.all()
        links = Link.objects.all()
        taskData = TaskSerializer(tasks, many=True)
        linkData = LinkSerializer(links, many=True)
        return Response({
            "tasks":taskData.data,
            "links":linkData.data,
        })