from django.db import models

class KakaoFriend(models.Model):

	name = models.CharField(max_length=200)
	type = models.CharField(max_length=200)
	job = models.CharField(max_length=200)
	age = models.IntegerField(default=0)

	def __str__(self):
		return self.name
# Create your models here.
