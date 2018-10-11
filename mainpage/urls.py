from django.urls import path
from . import views
from .views import Student

urlpatterns = [
    path('', Student.as_view(), name='index'),
]
