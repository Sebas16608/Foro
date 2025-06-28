from django.db import models
# Create your models here.

#Boards
class Board(models.Model):
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
