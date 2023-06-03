from rest_framework import serializers
from user.models import BackedUpFile

class BackedUpFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackedUpFile
        fields = '__all__'
