from django.db import models
from datetime import datetime
from django.forms import ModelForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class Pages(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    created = models.DateTimeField(auto_created=True, null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '%s - %s' % (self.pk, self.title)


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    page = models.ForeignKey(Pages, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s - %s' % (self.author.pk, self.pk, self.text)



