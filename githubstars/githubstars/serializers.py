from core.models import Repositorie
from rest_framework import serializers


class RepositorieSerializer(serializers.Serializer):
    repositorie_id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=255)
    language = serializers.CharField(max_length=20)
    tag = serializers.CharField(required=False, max_length=255)

    def create(self, validated_data):
        """ Create and return a new `Snippet` instance, given the validated data."""
        return Repositorie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Update and return an existing `Snippet` instance, given the validated data."""
        instance.repositorie_id = validated_data.get('repositorie_id', instance.repositorie_id)
        instance.name = validated_data.get('name', instance.name)
        instance.url = validated_data.get('url', instance.url)
        instance.language = validated_data.get('language', instance.language)
        instance.tag = validated_data.get('tag', instance.tag)
        instance.save()
        return instance
