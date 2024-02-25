from django.db import models
from django.utils.text import slugify

# Create your models here.


class Link(models.Model):
    """
    Links models by ndifoinhilary@gmail.com
    """

    name = models.CharField(max_length=200, unique=True)

    url = models.URLField(max_length=200)

    slug = models.SlugField(max_length=200, unique=True, blank=True)

    clicks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def click(self):
        self.clicks = self.clicks + 1
        self.save()
        return self.clicks

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
