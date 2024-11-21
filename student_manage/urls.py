from django.urls import path, include
from .views import list_student

urlpatterns = [
    path('', list_student, name='home'),
]
