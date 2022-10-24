from django.urls import path
from . import views

urlpatterns = [
    path('jawaban/', views.tampilkan_soal)
]