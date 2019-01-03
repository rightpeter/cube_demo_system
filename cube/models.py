from django.db import models


# Create your models here.
class Cell(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    county = models.CharField(max_length=30)
