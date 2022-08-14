from rest_framework import serializers

from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'slug', 'description')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    group = GroupSerializer(many=False, required=False)
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    post = serializers.SlugRelatedField(
        slug_field='id',
        queryset=Post.objects.all(),
        required=True
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
