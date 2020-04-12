from django.urls import path

from . import views

urlpatterns = [
    path('num3/', views.num3, name='num3'),
]
