from .models import Singer, Song
from rest_framework import serializers

# Hyperlinked model serializer will create a get link for the particular item0
class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration', 'url']

class SingerSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']