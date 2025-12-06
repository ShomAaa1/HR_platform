from rest_framework import viewsets
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import ResumePermissions
from rest_framework.permissions import IsAuthenticated


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated, ResumePermissions]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
