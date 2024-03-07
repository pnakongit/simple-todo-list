from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        to=Tag,
        related_name="tags",
        blank=True
    )
