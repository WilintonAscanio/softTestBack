from .models import SoftUserProject
from rest_framework import viewsets, permissions
from .serializers import SoftUserProjectSerializer

class SoftUserProjectViewSet(viewsets.ModelViewSet):
    queryset = SoftUserProject.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SoftUserProjectSerializer