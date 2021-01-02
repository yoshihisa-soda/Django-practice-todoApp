from django.db import models

# Create your models here.
CHOISE = (('danger', 'high'), ('warning', 'normal'), ('primary', 'low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices= CHOISE
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title
