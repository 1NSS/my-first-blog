from django.urls import path
from . import views

urlpatterns = [
    path('text2/', views.text2, name='text2'),

]