from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import EventSerializer
from .models import Event


class EventApiView(viewsets.ModelViewSet):
	queryset = Event.objects.all().order_by('-date')
	serializer_class = EventSerializer