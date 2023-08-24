from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import ClientSerializer,PolicySerializer
from .models import Client,Reminder,Policy
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class ClientList(generics.ListCreateAPIView): 
    queryset = Client.objects.all() 
    serializer_class = ClientSerializer

class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class PolicyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # new 
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

