from django.urls import path
from . import views

urlpatterns = [
    path('text2/text4/', views.text4, name='text4'),
]