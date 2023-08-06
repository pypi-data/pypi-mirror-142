from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models  import  Post,Category
from .serializer import  PostSerializer,PostDetailSerializer,CategorySerializer, CategoryDetailSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = Post.STATUS_NORMAL)
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)
    # permission_classes = [IsAdminUser]




class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset =  Category.objects.filter(status = Category.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = CategoryDetailSerializer
        return super().retrieve(request, *args, **kwargs)


