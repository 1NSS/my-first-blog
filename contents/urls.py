from django.urls import path
from . import views

urlpatterns = [
    path('text2/text4/add1/', views.add1, name='add1'),
    path('text2/text4/add2/', views.add2, name='add2'),
    path('text2/text4/add3/', views.add3, name='add3'),
    path('text2/text4/add4/', views.add4, name='add4'),
    path('text2/text4/add5/', views.add5, name='add5'),
    path('text2/text4/add6/', views.add6, name='add6'),
    path('text2/text4/add7/', views.add7, name='add7'),
    path('text2/text4/add8/', views.add8, name='add8'),
    path('text2/text4/add9/', views.add9, name='add9'),
    path('text2/text4/add10/', views.add10, name='add10'),
]