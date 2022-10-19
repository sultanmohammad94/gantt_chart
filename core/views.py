import json
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task, Link
from .serializers import TaskSerializer, LinkSerializer
from django.views.decorators.csrf import csrf_exempt

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
        
@api_view(['POST'])
def task_add(request):
    is_post_request = True if request.method == "POST" else False
    
    if is_post_request:
        print('Request ', request.data)
        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid():
            task = task_serializer.save()
            json_response = {
                'action': 'inserted',
                'tid': task.id
            }
            return JsonResponse(json_response)
        return JsonResponse({'action':'error'})
    
    
    
@api_view(['PUT','DELETE'])
def task_update(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        
    except Task.DoesNotExist:
        return JsonResponse({'action':'error2'})
    
    # Update
    if request.method == "PUT":
        task_serializer = TaskSerializer(task, data = request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse({"action":"updated"})
        return JsonResponse({'action':'error'})
    
    if request.method == "DELETE":
        task.delete()
        return JsonResponse({"action":"deleted"})
    
    

@api_view(['POST'])
def link_add(request):
    if request.method == 'POST':
        serializer = LinkSerializer(data=request.data)
        print(serializer)
 
        if serializer.is_valid():
            link = serializer.save()
            return JsonResponse({'action':'inserted', 'tid': link.id})
        return JsonResponse({'action':'error'})
 
@api_view(['PUT', 'DELETE'])
def link_update(request, pk):
    try:
        link = Link.objects.get(pk=pk)
    except Link.DoesNotExist:
        return JsonResponse({'action':'error'})
 
    if request.method == 'PUT':
        serializer = LinkSerializer(link, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'action':'updated'})
        return JsonResponse({'action':'error'})
 
    if request.method == 'DELETE':
        link.delete()
        return JsonResponse({'action':'deleted'})
    
@csrf_exempt
def get_erpnext_tasks(request):
    is_post = True if request.method == "POST" else False
    if is_post:
        json_data = {}
        post_data = dict(request.POST.lists())
        for data in post_data:
            json_data = json.loads(data)
          
        print(f'>>Json Data = {json_data}')   
        # is_group = json_data['is_group']
        # if is_group:
        #     task = Task.objects.create(
        #         text = json_data['subject'],
        #         start_date = json_data['exp_start_date'],
        #         end_date = json_data['exp_end_date'],
        #         duration = json_data['duration'],
        #         progress = json_data['progress'],
        #         parent = "0"
        #     )
        # elif not is_group:
        #     task = Task.objects.create(
        #         text = json_data['subject'],
        #         start_date = json_data['exp_start_date'],
        #         end_date = json_data['exp_end_date'],
        #         duration = json_data['duration'],
        #         progress = json_data['progress'],
        #         parent = json_data['parent_task']
        #     )
        # task.save()
        
    return HttpResponse("Hello ERP")