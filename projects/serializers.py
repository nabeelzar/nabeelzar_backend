from rest_framework import serializers
from projects.models import Project, ProjectImages, Technology


class TechnologySerializer(serializers.ModelSerializer):
	class Meta:
		model = Technology
		fields = '__all__'


class ProjectImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProjectImages 
		exclude = ('project',)


class ProjectSerializer(serializers.ModelSerializer):
	project_images = ProjectImageSerializer(many=True)
	technologies = TechnologySerializer(many=True)
	class Meta:
		model = Project 
		fields = ["id", "name", "description", "date_started", "date_completed", "technologies", "project_images"]