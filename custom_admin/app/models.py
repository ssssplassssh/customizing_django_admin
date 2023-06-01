from django.db import models

# Create your models here.

class MyModel(models.Model):
    field1 = models.CharField(max_length=50, default=1)
    field2 = models.CharField(max_length=50, default=1)
    field3 = models.CharField(max_length=50, default=1)
    
class RelatedModel(models.Model):
    field1 = models.CharField(max_length=50, default=1)
    field2 = models.CharField(max_length=50, default=1)
    field3 = models.CharField(max_length=50, default=1)
    field4 = models.CharField(max_length=50, default=1)
    field5 = models.CharField(max_length=50, default=1)