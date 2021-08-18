from django.db import models

# Create your models here.
class TodoList(models.Model):
    desc = models.CharField(max_length=150)