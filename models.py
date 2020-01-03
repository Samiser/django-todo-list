from django.db import models

# List of todo items
class List(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

# Todo items
class Item(models.Model):
    todo_list = models.ForeignKey(List, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.content
