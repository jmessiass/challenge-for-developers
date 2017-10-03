from core.models import Repositorie
from rest_framework import serializers


class RepositorieSerializer(serializers.Serializer):
    repositorie_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=255)
    language = serializers.CharField(max_length=20)
    tag = serializers.CharField(required=False, max_length=255)

    def create(self, validated_data):
        """ Create and return a new `Repositorie` instance, given the validated data."""
        return Repositorie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tag = validated_data.get('tag', instance.tag)
        return instance
