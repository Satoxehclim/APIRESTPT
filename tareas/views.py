from rest_framework import viewsets, permissions
from .models import Tarea
from .serializer import TareaSerializer
from django.shortcuts import render

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

