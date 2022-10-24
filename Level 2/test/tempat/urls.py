from django.urls import path
from . import views

urlpatterns = [
    path('soal/', views.tempat_menjawab)
]