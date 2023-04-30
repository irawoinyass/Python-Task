from rest_framework import generics, permissions, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, NestedCommentSerializer
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from users.permissions import IsUser
from categories.models import Category
from accounts.paginate import StandardResultsSetPagination

# Create a Post


@api_view(["POST"])
@permission_classes([IsAuthenticated, IsUser])
def create_post(request):
    user = request.user
    serializer = PostSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    qs = Post.objects.filter(
        author=user.id, title__iexact=request.data['title'])
    if qs.exists():
        return Response({"Error": f"{request.data['title']} Already Exists"})
    try:
        cat = get_object_or_404(Category, id=request.data['category_id'])
    except:
        return Response({"Error": "Category doesnot exist"}, status=404)

    serializer.save(author=user, category_id=cat)
    return Response("Created Successfully")


# List Post
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsUser])
def list_posts(request):
    user = request.user
    queryset = Post.objects.filter(author=user.id)
    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"})


# Publish
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsUser])
def publish_post(request, **kwargs):
    user = request.user

    try:
        post = get_object_or_404(
            Post, id=kwargs['post_id'], author=user.id)
    except:
        return Response({"Error": "Not Found"})

    post.is_public = True
    post.save()
    return Response("Published Successfully")

# UnPublish


@api_view(["GET"])
@permission_classes([IsAuthenticated, IsUser])
def un_publish_post(request, **kwargs):
    user = request.user

    try:
        post = get_object_or_404(
            Post, id=kwargs['post_id'], author=user.id)
    except:
        return Response({"Error": "Not Found"})

    post.is_public = False
    post.save()
    return Response("UnPublished Successfully")


# UPDATE
class PostUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = super(PostUpdateAPIView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


post_update_view = PostUpdateAPIView.as_view()

# Find API


class PostDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super(PostDetailAPIView,
                         self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


post_detail_view = PostDetailAPIView.as_view()


# Delete API


class PostDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = super(PostDestroyAPIView,
                         self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


post_destory_view = PostDestroyAPIView.as_view()


################################# Comment Section################################################################
# Make Comment
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsUser])
def create_comment(request):
    user = request.user
    serializer = CommentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        post = get_object_or_404(Post, id=request.data['post_id'])
        cat = get_object_or_404(Category, id=request.data['cat_id'])
        get_object_or_404(Post, id=request.data['post_id'],
                          category_id=request.data['cat_id'])
    except Exception as e:
        raise e

    serializer.save(post_id=post, user=user, cat_id=cat)
    return Response("Created Successfully")


# Update
class CommentUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = super(CommentUpdateAPIView,
                         self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


comment_update_view = CommentUpdateAPIView.as_view()

# Delete


class CommentDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = super(CommentDestroyAPIView,
                         self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


comment_destory_view = CommentDestroyAPIView.as_view()


############################################# Nested #######################################################################
# Create
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsUser])
def create_nestedcomment(request):
    user = request.user
    serializer = NestedCommentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        post = get_object_or_404(Post, id=request.data['post_id'])
        cat = get_object_or_404(Category, id=request.data['cat_id'])
        parent = get_object_or_404(Comment, id=request.data['parent'])
        get_object_or_404(Post, id=request.data['post_id'],
                          category_id=request.data['cat_id'])
    except Exception as e:
        raise e

    serializer.save(post_id=post, user=user, cat_id=cat, parent=parent)
    return Response("Created Successfully")


############################################## Public ###########################################################
# Fetch Comments with Post ID
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsUser])
def fetch_comments_by_post_id(request, **kwargs):
    user = request.user
    post_id = kwargs['post_id']

    queryset = Comment.objects.filter(post_id=post_id, parent=None)
    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"}, status=404)


# Fetch NestComments with Comment ID
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsUser])
def fetch_nestedcomments_by_post_id(request, **kwargs):
    user = request.user
    comment_id = kwargs['comment_id']

    queryset = Comment.objects.filter(parent=comment_id)
    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = NestedCommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"}, status=404)


# Fetch Post
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsUser])
def fetch_posts(request):
    user = request.user

    try:
        search = request.data['search']
        category_id = request.data['category_id']
        date = request.data['date']
    except Exception as e:
        raise e

    queryset = Post.objects.filter(is_public=True)

    if search:
        queryset = queryset.filter(title__icontains=search)
    if category_id:
        queryset = queryset.filter(category_id=category_id)
    if date:
        queryset = queryset.filter(posted_at__gte=date)

    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"}, status=404)


# fetch_comment
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsUser])
def fetch_comments(request):
    user = request.user

    try:
        search = request.data['search']
        cat_id = request.data['cat_id']
        date = request.data['date']
    except Exception as e:
        raise e

    queryset = Comment.objects.filter(parent=None)

    if search:
        queryset = queryset.filter(title__icontains=search)
    if cat_id:
        queryset = queryset.filter(cat_id=cat_id)
    if date:
        queryset = queryset.filter(created_at__gte=date)

    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"}, status=404)
