from django.db import models

# Create your models here.

class Size(models.Model):
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'
    sizes = ((SMALL, 'Small'), (MEDIUM, 'Medium'), (LARGE, 'Large'), (EXTRA_LARGE, 'Extra-Large'))
    size = models.CharField(max_length=10, choices=sizes, default=SMALL)

    def __str__(self):
        return self.size


class BackScratchers(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.CharField(max_length=100,blank=False, null=False)
    size = models.ManyToManyField(Size)

    def __str__(self):
        return self.name




