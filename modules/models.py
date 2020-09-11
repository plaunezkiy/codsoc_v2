from django.db import models


class Module(models.Model):
    title = models.TextField(max_length=120)
