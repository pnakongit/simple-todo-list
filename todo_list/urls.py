from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
]

app_name = "todo_list"
