from django.db import models
import uuid

class tasks(models.Model):
    taskData = models.CharField(max_length=200)
    taskID = models.UUIDField(default=uuid.uuid4, editable=False)
