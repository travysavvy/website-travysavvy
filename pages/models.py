from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    subject = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    message = models.TextField()
    send_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-send_on']

    def __str__(self):
        return self.subject