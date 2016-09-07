from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Fibonacci(models.Model):
  position = models.IntegerField()
  value = models.IntegerField()
  frequency = models.IntegerField()

  def __str__(self):
		return str(self.position)
