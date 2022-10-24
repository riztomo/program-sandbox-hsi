from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('evaluasi/', views.evaluasi),
    path('hasil/', views.hasil),
    path('admin/tambah-soal/', views.tambah),
    path('admin/ubah-soal/<int:id>', views.ubah),
    path('admin/daftar-soal/', views.daftar),
    path('admin/', views.admin)
]