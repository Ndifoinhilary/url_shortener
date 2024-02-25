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

    def click(self, request=None):
        # Check if the link has already been clicked in this session
        if request and "clicked_links" not in request.session:
            request.session["clicked_links"] = set()

        if request and self.id not in request.session["clicked_links"]:
            # Link hasn't been clicked in this session, increment the count
            self.clicks += 1

            # Mark the link as clicked in this session
            request.session["clicked_links"].add(self.id)
            request.session.modified = True  # Ensure the session is saved

            self.save()

        return self.clicks

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
