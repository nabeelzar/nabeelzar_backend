from django.db import models
import datetime

# many to many (multiple projects can have multiple technologies)
class Technology(models.Model):
	name = models.CharField(max_length=45)
	img_path = models.CharField(max_length=45, default="/")
	def __str__(self):
		return f"{self.name}:{self.img_path}"


class Project(models.Model):
	name = models.CharField(max_length=45)
	description = models.TextField()
	date_started = models.DateField(default=datetime.date.today())
	date_completed = models.DateField(null=True, blank=True)

	technologies = models.ManyToManyField(Technology)

	def __str__(self):
		return f"{self.name}" 


# one to many (many images for one project)
class ProjectImages(models.Model):
	project = models.ForeignKey(Project, related_name='project_images', on_delete=models.CASCADE)
	img_path = models.CharField(max_length=45, default="/")
	main = models.BooleanField(default=False)

