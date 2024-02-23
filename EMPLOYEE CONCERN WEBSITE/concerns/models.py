from django.db import models

# Create your models here.
from django.db import models


class Concern(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employee_name = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
