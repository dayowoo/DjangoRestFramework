from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FilesSerialzier
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status



class PostViewSet(viewsets.ModelViewSet):
    
    # 필수
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    # 검색
    filter_backends = [SearchFilter]
    SearchFilter = ('title', 'body')    #회원검색: 'author'


    # 자동저장 method
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)       # 내가 작성한 user의 author

    # 현재 request를 보낸 유저
    # == self.request.user

    # 필터링
    def get_queryset(self):
        qs = super().get_queryset()
        
        if self.request.user.is_authenticated:
            qs = qs.filter(author = self.request.user)
        else:
            qs = qs.none()
        return qs


class ImageViewSet(viewsets.ModelViewSet):
    
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer




class FilesViewSet(viewsets.ModelViewSet):
    
    # parser_class 저장 / 다양한 미디어 타입으로 request를 수락하는 방법 중 하나
    parser_classes = (MultiPartParser, FormParser)
    
    queryset = Files.objects.all()
    serializer_class = FilesSerialzier

    # create() 오버라이딩
    # API HTTP -> get() post() 

    # create() -> post()
    def post(self, request, *args, **kwargs):
        serializer = FilesSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
