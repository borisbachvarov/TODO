from rest_framework import viewsets
from rest_framework.response import Response

from .models import ToDoList, ToDoItem
from .serializers import TodoListSerializer, TodoItemSerializer

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = TodoListSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Custom logic before deletion
        instance.delete()
        return Response({"message": "Item deleted successfully"}, status=204)

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = TodoItemSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Custom logic before deletion
        instance.delete()
        return Response({"message": "Item deleted successfully"}, status=204)