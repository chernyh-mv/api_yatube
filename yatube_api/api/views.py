from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from posts.models import Comment, Group, Post
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


    def perform_destroy(self, serializer):
        serializer.delete()


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        queryset = Comment.objects.filter(post=post)
        return queryset
