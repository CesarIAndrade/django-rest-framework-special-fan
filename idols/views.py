from rest_framework import permissions, viewsets
from .serializers import IdolSerializer
from .models import Idol


class IdolViewSet(viewsets.ModelViewSet):
    queryset = Idol.objects.all()
    serializer_class = IdolSerializer
    permission_classes = [permissions.AllowAny]
