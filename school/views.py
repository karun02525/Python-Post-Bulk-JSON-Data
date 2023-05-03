from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import response,status
from .models import Student,Teacher
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.

def home(request):
    create_bulk()

@api_view(['POST'])
def create(request):
    serializer  = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':False,'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response({'status':True,'message':'successfull create','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get(request):
    query_set = Student.objects.all()
    serializer = StudentSerializer(query_set,many=True)
    return Response({'status':True,'data':serializer.data},status=status.HTTP_200_OK)


@api_view(['POST'])
def create_bulk(request):
    items = request.data.get('items')
    '''items = [
       {
      "name": "VNS Bokari School",
      "city": "Bokaro",
      "age": 23
    },
    {
      "name": "Dhar SViS  School",
      "city": "Dhanbad",
      "age": 22
    }] '''
    bulk_list = []
    for item in items:
        bulk_list.append(Teacher(name=item.get('name'),age=item.get('age'),city=item.get('city')))
    Teacher.objects.bulk_create(bulk_list)    
    return Response({'status':True,'message':'all data create successfull'},status=status.HTTP_201_CREATED)
  
    
   
        