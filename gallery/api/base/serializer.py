from rest_framework import serializers
from gallery.models import Group
from gallery.models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = ('group_id', 'group_name', 'photos', 'user')

    def get_photos(self, obj):
        no_of_photos = obj.photos.values().count()
        return no_of_photos
