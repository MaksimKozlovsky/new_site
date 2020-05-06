from django.db import models

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.pk, self.title)