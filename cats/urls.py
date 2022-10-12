from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cats import views

urlpatterns = [
    path('', views.CatObj.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)