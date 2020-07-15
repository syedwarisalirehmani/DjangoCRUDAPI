from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .serializers import UserSerializer
from rest_framework.decorators import api_view
from .models import User
from rest_framework.response import Response


# Create your views here.

@api_view(['POST'])
def userCreate(request):
    user_serializer = UserSerializer(date=request.data, many=True)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data)


@api_view(['GET'])
def getUser(request):
    object_all = User.objects.all()
    serializer = UserSerializer(object_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detailUser(request, id):
    object_all = User.objects.get(id=id)
    serializer = UserSerializer(object_all, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def userUpdate(request, id):
    object_all = User.objects.get(id=id)
    user_serializer = UserSerializer(instance=object_all, date=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data)


@api_view(['DELETE'])
def deleteUser(request, id):
    user_object = User.objects.get(id=id)
    user_object.delete()
    return Response("Item successfully deleted")


def getDemo(request):
    return HttpResponse("this is the html")
