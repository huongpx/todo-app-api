from django.urls import path, include


urlpatterns = [
    path('todos/', include('todolist.apps.todos.urls')),
    path('accounts/', include('todolist.apps.accounts.urls')),
]