from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    permission_classes = [AllowAny]
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'password']

        def create(self, validated_data):
            user = User.objects.create_user(
                username=validated_data['userame'],
                password=validated_data['password'],
            )
            return user
