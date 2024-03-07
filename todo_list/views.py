from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task, Tag


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


class ToggleTaskStatusView(generic.RedirectView):
    url = reverse_lazy("todo_list:index")

    def get(self, request, *args, **kwargs) -> HttpResponseRedirect:
        pk_from_kwargs = self.kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk_from_kwargs)
        task.is_completed = not task.is_completed
        task.save()
        return super().get(request, *args, **kwargs)


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("todo_list:tag_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("todo_list:tag_list")
