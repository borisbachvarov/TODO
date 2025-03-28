from django.urls import path
from rest_framework.routers import DefaultRouter
from .api_views import TodoListViewSet, TodoItemViewSet

router = DefaultRouter()
router.register(r'lists', TodoListViewSet, basename='list')
router.register(r'items', TodoItemViewSet, basename='item')

urlpatterns = router.urls
