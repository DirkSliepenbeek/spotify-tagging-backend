from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
from spotify_tagging.models import Track, Tag, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['__all__']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = self.Meta.model()
        user.set_password(validated_data['password'])
        user.save()
        return user


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Track
        fields = '__all__'
        extra_fields = ['tags']


class ProjectSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = '__all__'
        extra_fields = ['tracks', 'tags']
