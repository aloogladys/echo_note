from rest_framework.response  import Response 
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from echo_app.models import User 


@api_view(['GET'])
def getallData(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many = True)
    return Response(serializer.data )

@api_view(['GET'])
def getoneData(request,id):
    user = User.objects.get(id=id)
    serializer = UserSerializer(user, many =False )
    return Response(serializer.data)

@api_view(['POST'])
def addData(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)

@api_view(['PUT'])
def updateData(request,id):
    user = User.objects.get(id=id)
    serializer =UserSerializer(instance =user )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteData(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return Response()