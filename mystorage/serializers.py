from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')

class AlbumSerializer(serializers.ModelSerializer):
    
    author_name = serializers.ReadOnlyField(source='author.username')
    # 이미지 업로드->결과값 받음: 확인작업을 url로 하겠다.
    image = serializers.ImageField(use_url=True)    

    class Meta:
        model = Album
        fields = ('pk', 'image', 'desc', 'author_name')



class FilesSerialzier(serializers.ModelSerializer):
    
    author = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url=True)    

    class Meta:
        model = Album
        fields = ('pk', 'myfile', 'desc', 'author')