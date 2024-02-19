from django.db import models

class Experience(models.Model):
    organizationName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    startDate = models.DateField()
    endDate = models.DateField()