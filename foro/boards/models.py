from django.db import models
# Create your models here.

#Boards
class Board(models.Model):
    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"/{self.short_name}/ - {self.name}"

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Boards"
        ordering = ['short_name']
