from django.shortcuts import render

# Create your views here.

import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer, CustomUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    # ここでfilterをかけてやれば大丈夫
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(name="pokotsun")
    serializer_class = CustomUserSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = ('author', 'status')

