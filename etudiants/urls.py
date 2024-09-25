# etudiants/urls.py

from django.urls import path
from .views import EtudiantListCreateView, EtudiantRetrieveUpdateDestroyView

urlpatterns = [
    path('etudiants/', EtudiantListCreateView.as_view(), name='etudiant-list-create'),
    path('etudiants/<int:pk>/', EtudiantRetrieveUpdateDestroyView.as_view(), name='etudiant-detail'),
]
