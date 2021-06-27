from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=60)
    address = models.TextField(max_length=200)
    pieces = models.FloatField()

    def __str__(self):
        return self.name
