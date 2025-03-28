from .models import ToDoItem, ToDoList
from rest_framework import serializers

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'created_date', 'due_date', 'todo_list']

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['title']