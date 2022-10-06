from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from delpeople import views

urlpatterns = [
    path('', views.PersonList.as_view()),
    path('<int:pk>/', views.PersonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)