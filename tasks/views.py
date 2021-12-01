from django.http import HttpResponse
from .models import Task
from .serializer import TaskSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


@api_view(['POST', 'DELETE'])
def task_detail(request, pk):
    """
    Retrieve, update or delete a task.
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    #     get_task = Task.objects.all()
    #     serializer_json = serializers.serialize("json", get_task)
    #     return HttpResponse(serializer_json, content_type="application/json")

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(request.data,  content_type="application/json", status=status.HTTP_201_CREATED)
        return HttpResponse(request.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        serializer_json = serializers.serialize("json", task)
        return HttpResponse(serializer_json, content_type="application/json", status=status.HTTP_200_OK)


@api_view(['GET'])
def get_task(request):
    get_task = Task.objects.all()
    serializer_json = serializers.serialize("json", get_task)
    return HttpResponse(serializer_json, content_type="application/json", status=status.HTTP_200_OK)
