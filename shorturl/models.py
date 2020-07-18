from django.db import models

class Url(models.Model):
	url = models.CharField(max_length=200)
	shortUrl = models.CharField(max_length=200)

	def __init__():
		return self.url


