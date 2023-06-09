from rest_framework import serializers
from .models import Post, Comment


class WhoCommentPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class PostPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    body = serializers.CharField(read_only=True)
    posted_at = serializers.DateField(read_only=True)


class WhoPostedPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class CategoryPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category_name = serializers.CharField(read_only=True)


class PrimaryCommentPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    comment = serializers.CharField(read_only=True)
    created_at = serializers.DateField(read_only=True)


class PostSerializer(serializers.ModelSerializer):
    who_posted = WhoPostedPublicSerializer(
        source='author', read_only=True)
    category = CategoryPublicSerializer(
        source='category_id', read_only=True)
    category_id = serializers.CharField()

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'category_id',
            'posted_at',
            'is_public',
            'who_posted',
            'category'

        ]


class CommentSerializer(serializers.ModelSerializer):
    # nested = NestedCommentPublicSerializer(
    #     source='posts.NestedComment', read_only=True)
    post = PostPublicSerializer(
        source='post_id', read_only=True)
    who_comment = WhoCommentPublicSerializer(
        source='user', read_only=True)

    category = CategoryPublicSerializer(
        source='cat_id', read_only=True)

    post_id = serializers.CharField()
    cat_id = serializers.CharField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'post_id',
            'cat_id',
            'comment',
            'created_at',
            'post',
            'category',
            'who_comment',
            # 'nested',

        ]


class NestedCommentSerializer(serializers.ModelSerializer):
    # nested = NestedCommentPublicSerializer(
    #     source='posts.NestedComment', read_only=True)
    post = PostPublicSerializer(
        source='post_id', read_only=True)
    who_comment = WhoCommentPublicSerializer(
        source='user', read_only=True)

    category = CategoryPublicSerializer(
        source='cat_id', read_only=True)

    post_id = serializers.CharField()
    cat_id = serializers.CharField()
    parent = serializers.CharField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'post_id',
            'parent',
            'cat_id',
            'comment',
            'created_at',
            'post',
            'category',
            'who_comment',
            # 'nested',

        ]
