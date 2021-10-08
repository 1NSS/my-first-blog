from django.urls import path
from . import views

urlpatterns = [
    path('text2/text4/', views.Text4View.as_view(), name='text4'),
]