from rest_framework import viewsets
from user.api.serializers import BackedUpFileSerializer
from user.models import BackedUpFile

class BackedUpFileViewSet(viewsets.ModelViewSet):
    queryset = BackedUpFile.objects.all()
    serializer_class = BackedUpFileSerializer
    # Implement additional permissions and filtering as needed
