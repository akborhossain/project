from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.authentication import TokenAuthentication
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes=[TokenAuthentication]
    #permission_classes = [IsAdminOrReadOnly]
    def perform_create(self, serializer):
        username = self.request.user
        serializer.save(username=username)