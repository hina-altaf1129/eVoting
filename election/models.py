from django.db import models

# Create your models here.


class Party(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=50)


class Candidate(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
