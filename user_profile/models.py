from django.db import models

# Create your models here.
class zonal_tweets(models.Model):
	tag   = models.CharField(max_length=10)
	tweet = models.TextField()

	def __str__(self):
		return self.tag
