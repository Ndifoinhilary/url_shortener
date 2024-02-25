from django.db import models

# Create your models here.


class Link(models.Model):
    """
    Links models by ndifoinhilary@gmail.com
    """

    name = models.CharField(max_length=200, unque=True)
