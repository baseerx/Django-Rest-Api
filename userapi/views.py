from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import UserModel
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    queryset = UserModel.objects.all()
    serializer = UserSerializer(queryset, many=True)
    data=serializer.data
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User created successfully'})
    return Response({'message': 'User not created'})

@api_view(['GET'])
def userDetail(request, pk):
	tasks = UserModel.objects.get(id=pk)
	serializer = UserSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def userUpdate(request, pk):
	task = UserModel.objects.get(id=pk)
	serializer = UserSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def userDelete(request, pk):
	task = UserModel.objects.get(id=pk)
	task.delete()

	return Response('Item successfully deleted!')
