from django.db import models

class Meal(models.Model):
    """Model to populate meal data from the DB API with."""

    id = models.CharField(max_length=50, blank = True, primary_key=True)
    name = models.CharField(max_length=50, blank = True, null = True)
    category = models.CharField(max_length=10, blank = True, null = True)
    instructions = models.CharField(max_length=4000, blank = True, null = True)
    region = models.CharField(max_length=20, blank = True, null = True)
    slug = models.SlugField(default = 'test')
    image_url = models.CharField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.name