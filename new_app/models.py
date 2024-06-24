from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    engine = models.IntegerField(null=True, blank=True)
    price = models.FloatField()
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name
