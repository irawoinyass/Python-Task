from rest_framework import serializers
from accounts.serializers import NestedCommentPublicSerializer, PostPublicSerializer, WhoCommentPublicSerializer, WhoPostedPublicSerializer, CategoryPublicSerializer, PrimaryCommentPublicSerializer
from .models import Post, Comment, NestedComment


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
    who_comment = WhoCommentPublicSerializer(
        source='user', read_only=True)
    primary_comment = PrimaryCommentPublicSerializer(
        source='comment_id', read_only=True)
    comment_id = serializers.CharField()

    class Meta:
        model = NestedComment
        fields = [
            'id',
            'comment_id',
            'comment',
            'created_at',
            'who_comment',
            'primary_comment'
        ]
