# todo_app/urls.py
from django.urls import path, include
from .views import UserRegisterViewSet, TodoViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'register', UserRegisterViewSet, basename='register')
router.register(r'todos', TodoViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
