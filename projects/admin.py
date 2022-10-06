from django.contrib import admin
from projects.models import Project, Technology, ProjectImages

admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(ProjectImages)