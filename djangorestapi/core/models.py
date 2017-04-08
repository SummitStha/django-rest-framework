from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length = 20)
	location = models.CharField(max_length = 20)
	date = models.DateField()

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name