from rest_framework import serializers
from .models import (
    Organization,
    UserProfile,
)


class Organizationserializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'