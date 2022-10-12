from django.db import models

# Create your models here.
class Cat(models.Model):
	source_name = models.CharField(max_length=50, unique=True) 
	redditor = models.CharField(blank=True, null=True, max_length=50)
	img_path = models.ImageField(upload_to="images/cats")

	def __str__(self):
		return f"{self.source_name}:{self.img_path}"