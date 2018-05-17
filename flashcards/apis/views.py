# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from rest_framework import viewsets
from .serializers import SlowaSerializer, DefinicjeSerializer


# Create your views here.

class SlowaViewSet(viewsets.ModelViewSet):
    queryset = Slowa.objects.all().order_by('-id_slowo')
    serializer_class = SlowaSerializer

class DefinicjeViewSet(viewsets.ModelViewSet):
    queryset = Definicje.objects.all().order_by('-id_definicja')
    serializer_class = DefinicjeSerializer
