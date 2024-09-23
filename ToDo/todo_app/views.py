# todo_app/views.py
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, TodoSerializer
from .models import TodoModel
from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

User = get_user_model()

class TodoFilter(filters.FilterSet):
    completed = filters.BooleanFilter(field_name='completed', required=False)  # Optional filter for completed status

    class Meta:
        model = TodoModel
        fields = ['completed']

class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]  # Allow registration without authentication

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = TodoFilter

    def get_queryset(self):
        return TodoModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
