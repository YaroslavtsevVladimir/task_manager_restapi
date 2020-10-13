from django.db import models


class Task(models.Model):
    class Priority(models.TextChoices):
        MINOR = 'MN', 'Minor'
        MAJOR = 'MJ', 'Major'

    class Status(models.TextChoices):
        NEW = 'NEW', 'New'
        PLANNED = 'PLN', 'Planned'
        IN_PROGRESS = 'PRG', 'In Progress'
        DONE = 'DON', 'Done'

    class Meta:
        ordering = ['-priority']

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NEW)
    created = models.DateField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    deadline = models.DateField(null=True)
    priority = models.CharField(max_length=5, default=Priority.MINOR, choices=Priority.choices)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(null=True)

    def __str__(self):
        return self.title
