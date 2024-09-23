# todo_app/serializers.py
from rest_framework import serializers
from .models import CustomUser, TodoModel

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id', 'title', 'description', 'completed', 'user']
        read_only_fields = ['user']
