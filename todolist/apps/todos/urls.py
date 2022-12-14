from django.urls import path

from .views import TodosList, TodoDetail


urlpatterns = [
    path('/', TodosList.as_view()),
    path('<int:pk>/', TodoDetail.as_view()),
]
