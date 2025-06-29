from django.db import models
from boards.models import Board
import random
import string

def generar_anon_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

class Thread(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='threads')
    titulo = models.CharField(max_length=50, blank=True)
    contenido = models.TextField(blank=False)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    bump = models.DateTimeField(auto_now_add=True)
    anon_id = models.CharField(max_length=8, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.anon_id:
            self.anon_id = generar_anon_id()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.titulo or '[Sin título]'} ({self.board.short_name})"
    
    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"
        ordering = ['-bump']  # los hilos más activos primero
