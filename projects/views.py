from projects.models import Project 
from projects.serializers import ProjectSerializer

from rest_framework import mixins
from rest_framework import generics

class ProjectList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Project.objects.all().order_by("-date_started")
    serializer_class = ProjectSerializer 

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
