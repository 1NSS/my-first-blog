from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('text2/text4/', views.Text4View.as_view(), name='text4'),
=======
    path('text2/text4/', views.text4, name='text4'),
>>>>>>> 0d32a521784c8e6e4bf4c6a6d6fe53c577394d37
]