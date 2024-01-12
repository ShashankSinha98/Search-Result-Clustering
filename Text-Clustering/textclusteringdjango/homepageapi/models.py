from django.db import models

# Create your models here.
class Query(models.Model):
    query = models.CharField(max_length=200)
    k_value = models.IntegerField()