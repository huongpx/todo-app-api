from rest_framework import generics

from .models import Todos
from .serializers import TodosSerializer


class TodosList(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    
    
class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
