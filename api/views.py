from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from api.serializers import TypeSerializer
from api.serializers import RoomSerializer
from api.serializers import ClientSerializer

from hotel.models import Type
from hotel.models import Room
from hotel.models import Client

# Create your views here.
class TypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint para Tipos
    """
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]
class RoomViewSet(viewsets.ModelViewSet):
    """
    API endpoint para Habitaciones
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint para Clientes
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]