from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task


class TaskListView(generic.ListView):
    model = Task
    ordering = ("is_completed", "-created_at")

    def get_queryset(self) -> QuerySet:
        task_qs = Task.objects.all().prefetch_related("tags")
        if self.get_ordering():
            return task_qs.order_by(*self.get_ordering())
        return task_qs


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ("content", "deadline", "is_completed", "tags")
    success_url = reverse_lazy("todo_list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ("content", "deadline", "is_completed", "tags")
    success_url = reverse_lazy("todo_list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:index")
    template_name = "todo_list/confirm_delete.html"
