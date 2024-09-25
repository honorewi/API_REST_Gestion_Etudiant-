from rest_framework import generics
from .models import Etudiant
from .serializers import EtudiantSerializer

class EtudiantListCreateView(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class=EtudiantSerializer

class EtudiantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

# Create your views here.
