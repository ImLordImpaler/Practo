from django.shortcuts import render
from rest_framework.response import Response
from .models import Doctor
from .serializers import doctorSerializer
from  rest_framework.decorators import api_view


@api_view(['GET'])
def doctor(request):
    docs = Doctor.objects.all()
    serializer = doctorSerializer(docs , many=True)

    return  Response(serializer.data)

@api_view(['POST'])
def addDoctor(request):
    serial = doctorSerializer(data=request.data )
    if serial.is_valid():
        serial.save()
    return  Response(serial.data)


def newAppoint(request):
    pass