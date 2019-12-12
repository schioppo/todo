# posts/serializers.py
from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'date', 'author', 'done',)
        model = Todo