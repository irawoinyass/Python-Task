from rest_framework import generics, permissions, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post, Comment, NestedComment
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
        return Response({"Error": "Category doesnot exist"})

    serializer.save(author=user, category_id=cat)
    return Response("Created Successfully")


# List Post
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsUser])
def list_posts(request):
    user = request.user
    # queryset = Post.objects.filter(author=user.id)
    # data = PostSerializer(
    #     queryset, many=True).data
    # return Response({"data": data})
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
    except:
        return Response({"Error": "Category doesnot exist"})

    try:
        cat = get_object_or_404(Category, id=request.data['cat_id'])
    except:
        return Response({"Error": "Category doesnot exist"})

    try:
        get_object_or_404(Post, id=request.data['post_id'],
                          category_id=request.data['cat_id'])
    except:
        return Response({"Error": "Post and Category doesnt align"})

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
        com = get_object_or_404(Comment, id=request.data['comment_id'])
    except:
        return Response({"Error": "Comment doesnot exist"})

    serializer.save(comment_id=com, user=user)
    return Response("Created Successfully")


# Update
class NestedCommentUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    queryset = NestedComment.objects.all()
    serializer_class = NestedCommentSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = super(NestedCommentUpdateAPIView,
                         self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


nestedcomment_update_view = NestedCommentUpdateAPIView.as_view()

# Delete


class NestedCommentDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    queryset = NestedComment.objects.all()
    serializer_class = NestedCommentSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = super(NestedCommentDestroyAPIView,
                         self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


nestedcomment_destory_view = CommentDestroyAPIView.as_view()


############################################## Public ###########################################################
# Fetch Comments with Post ID
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsUser])
def fetch_comments_by_post_id(request, **kwargs):
    user = request.user
    post_id = kwargs['post_id']

    queryset = Comment.objects.filter(post_id=post_id)
    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"})


# Fetch NestComments with Comment ID
@api_view(["GET"])
@permission_classes([IsAuthenticated, IsUser])
def fetch_nestedcomments_by_post_id(request, **kwargs):
    user = request.user
    comment_id = kwargs['comment_id']

    queryset = NestedComment.objects.filter(comment_id=comment_id)
    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = NestedCommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"})


# Fetch Post
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsUser])
def fetch_posts(request):
    user = request.user

    try:
        search = request.data['search']
    except:
        return Response({"Error": "Include Search Field"})

    try:
        category_id = request.data['category_id']
    except:
        return Response({"Error": "Include Category ID Field"})

    try:
        date = request.data['date']
    except:
        return Response({"Error": "Include Date Field"})

    # Search Only
    if search != "" and category_id == "" and date == "":
        queryset = Post.objects.filter(title__icontains=search, is_public=True)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # Category Only
    if search == "" and category_id != "" and date == "":
        queryset = Post.objects.filter(category_id=category_id, is_public=True)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # Date Only
    if search == "" and category_id == "" and date != "":
        queryset = Post.objects.filter(
            posted_at__gte=date, is_public=True)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

        # Search,  Caegory, Date
    if search != "" and category_id != "" and date != "":
        queryset = Post.objects.filter(title__icontains=search).filter(category_id=category_id).filter(
            posted_at__gte=date).filter(is_public=True)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

        # Search,  Caegory
    if search != "" and category_id != "" and date == "":
        queryset = Post.objects.filter(title__icontains=search).filter(
            category_id=category_id).filter(is_public=True)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

         # Search, Date
    if search != "" and category_id == "" and date != "":
        queryset = Post.objects.filter(title__icontains=search).filter(
            posted_at__gte=date).filter(is_public=True)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # Caegory, Date
    if search == "" and category_id != "" and date != "":
        queryset = Post.objects.filter(category_id=category_id).filter(
            posted_at__gte=date).filter(is_public=True)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # default
    queryset = Post.objects.filter(is_public=True)
    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"})


# fetch_comment
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsUser])
def fetch_comments(request):
    user = request.user

    try:
        search = request.data['search']
    except:
        return Response({"Error": "Include Search Field"})

    try:
        cat_id = request.data['cat_id']
    except:
        return Response({"Error": "Include Category ID Field"})

    try:
        date = request.data['date']
    except:
        return Response({"Error": "Include Date Field"})

    # Search Only
    if search != "" and cat_id == "" and date == "":
        queryset = Comment.objects.filter(
            title__icontains=search)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = CommentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # Category Only
    if search == "" and cat_id != "" and date == "":
        queryset = Comment.objects.filter(cat_id=cat_id)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = CommentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # Date Only
    if search == "" and cat_id == "" and date != "":
        queryset = Comment.objects.filter(
            created_at__gte=date)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = CommentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

        # Search,  Caegory, Date
    if search != "" and cat_id != "" and date != "":
        queryset = Comment.objects.filter(title__icontains=search).filter(cat_id=cat_id).filter(
            created_at__gte=date)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = CommentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

        # Search,  Caegory
    if search != "" and cat_id != "" and date == "":
        queryset = Comment.objects.filter(title__icontains=search).filter(
            cat_id=cat_id)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = CommentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

         # Search, Date
    if search != "" and cat_id == "" and date != "":
        queryset = Comment.objects.filter(title__icontains=search).filter(
            created_at__gte=date)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = CommentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # Caegory, Date
    if search == "" and cat_id != "" and date != "":
        queryset = Comment.objects.filter(cat_id=cat_id).filter(
            created_at__gte=date)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = CommentSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # default
    queryset = Comment.objects.all()
    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = CommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"})
