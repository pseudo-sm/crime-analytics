from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=140,null=True,blank=True)
	body = models.TextField(null=True,blank=True)
	date = models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):
		return self.title



