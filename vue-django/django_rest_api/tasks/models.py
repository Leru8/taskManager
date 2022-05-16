from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    stage = models.CharField(null = True, max_length = 10, default="ToDo")
    created_at = models.DateField(auto_now_add = True)
    timer = models.IntegerField(null=True, default=0)
    timerState = models.BooleanField(default=False)

    def __str__(self):
        return self.title
