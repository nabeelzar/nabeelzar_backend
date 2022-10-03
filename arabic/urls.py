from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from arabic import views

from rest_framework import routers

urlpatterns = [
    path('sentence', views.ArabicSentence.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)