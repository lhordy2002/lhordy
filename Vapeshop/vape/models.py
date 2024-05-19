from django.db import models

class vape(models.Module):
    name = models.charField(max_length=225)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField()
