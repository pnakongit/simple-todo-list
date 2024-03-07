from django.db.models import QuerySet
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
