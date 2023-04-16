from rest_framework import serializers


class NestedCommentPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    comment = serializers.CharField(read_only=True)
    created_at = serializers.DateField(read_only=True)


class PostPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    body = serializers.CharField(read_only=True)
    posted_at = serializers.DateField(read_only=True)


class WhoCommentPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


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
