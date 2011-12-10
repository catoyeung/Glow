from django.db import models

class Account(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField(max_length=75)
