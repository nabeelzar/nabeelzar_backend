from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views

urlpatterns = [
    path('', views.ProjectList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)