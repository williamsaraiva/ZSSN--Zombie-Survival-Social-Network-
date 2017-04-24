from django.db.models import Count
from django.shortcuts import render

from .models import survivor_control, survivor, infected, inventory
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .Serializers import survivor_controlSerializer, survivorSerializer, infectedSerializer,inventorySerializer


# Create your views here.

class survivor_controlViewSet(viewsets.ModelViewSet):
    queryset = survivor_control.objects.all().order_by('-created')
    serializer_class = survivor_controlSerializer


class survivorViewSet(viewsets.ModelViewSet):
    queryset = survivor.objects.all().order_by('-created')
    serializer_class = survivorSerializer

class infectedViewSet(viewsets.ModelViewSet):
    queryset = infected.objects.all().order_by('-created')
    serializer_class = infectedSerializer

class invetoryViewSet(viewsets.ModelViewSet):
    queryset = inventory.objects.all().order_by('-created')
    serializer_class = inventorySerializer



