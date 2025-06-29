from django.db import models
from threads.models import Thread
import random
import string

def generar_anon_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    anon_id = models.CharField(max_length=8, editable=False, unique=True)
    es_op = models.BooleanField(default=False)
    borrado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.anon_id:
            self.anon_id = generar_anon_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Post #{self.id} en hilo {self.thread.id} - {self.anon_id}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['creado']
