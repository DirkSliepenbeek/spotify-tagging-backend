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

    def create(self, request, *args, **kwargs):
        project, created = Project.objects.get_or_create(users=request.user)
        # TODO change later when users can create projects
        track = request.data['track']
        tags = request.data['tags']
        artists = [artist['name'] for artist in track['artists']]
        tags = [self.get_or_create_helper(project, tag_name) for tag_name in tags]
        track, created = Track.objects.get_or_create(project=project, name=track['name'], uri=track['uri'],
                                                     artists=artists, album=track['album']['name'])
        track.tags.set(tags)
        serializer = app_serializers.TrackSerializer(track)

        return Response(serializer.data)

    @staticmethod
    def get_or_create_helper(project, tag_name):
        instance, created = Tag.objects.get_or_create(project=project, name=tag_name)
        return instance


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = app_serializers.ProjectSerializer
