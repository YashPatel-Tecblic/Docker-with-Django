
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from rest_framework import status
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def getdata(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data,status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response({'msg':'Data Created successfully'})

@api_view(['PUT'])
def updateUser(request,pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response({'msg':'Data updated Successfully!'})
    

@api_view(['DELETE'])
def deleteUser(request,pk):
    user = User.objects.get(id =pk)
    user.delete()
    return Response('User Successfully Deleted!')