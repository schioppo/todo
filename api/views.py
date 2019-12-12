from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import TodoSerializer
from .permissions import IsAuthorOrReadOnly
from todo.models import Todo
# Create your views here.
class TodoApiList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoApiDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
