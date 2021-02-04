from rest_framework import serializers
from sendfiles.models import *


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =serializers.FileField(max_length=None, allow_empty_file=False)
        fields = ('date_add', 'name', 'link')
    

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name')