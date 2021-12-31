from rest_framework.response import Response

from spotify_tagging.models import User, Tag, Track, Project
from rest_framework import viewsets
import spotify_tagging.serializers as app_serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = app_serializers.UserSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = app_serializers.TagSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = app_serializers.TrackSerializer

    def create(self, request,  *args, **kwargs):
        print(request.data)
        queryset = User.objects.all()
        serializer = app_serializers.TrackSerializer(queryset, many=True)
        return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = app_serializers.ProjectSerializer
