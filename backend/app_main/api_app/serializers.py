from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=64, required=False)
    email = serializers.CharField(max_length=64, required=False)
    phone = serializers.CharField(max_length=64, required=False)
    website = serializers.CharField(max_length=64, required=False)
    address = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = Contact
        fields = ('__all__')