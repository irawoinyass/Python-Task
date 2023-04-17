from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer
from accounts.models import User
from .permissions import IsSuperUser, IsSuperUserTwo
from categories.models import Category
from posts.models import Post, Comment, NestedComment
from posts.serializers import PostSerializer, CommentSerializer
from accounts.paginate import StandardResultsSetPagination

# ADMIN LOGIN API


@api_view(["POST"])
@permission_classes([AllowAny])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

    # pass
    if user.is_superuser:
        return Response({
            'admin_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'name': user.name,
            },
            'token': token
        })
    return Response({"Error": "UnAuthorized User"})


# GET ADMIN INFO
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_admin_data(request):
    user = request.user
    if user.is_superuser:
        return Response({
            'admin_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'name': user.name
            }
        })
    return Response({"Error": "UnAuthorized User"})


# Create Admin User API
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_admin_user(request):
    user = request.user

    if user.is_superuser:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Created Successfully"})

    return Response({"Error": "UnAuthorized User"})


# Update Update Admin user
class UpdateAdminUserAPIView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = User.objects.filter(is_staff=True, is_superuser=False)
    serializer_class = RegisterSerializer
    lookup_field = 'pk'


adminuser_update_view = UpdateAdminUserAPIView.as_view()


# List Admin User
class AdminUserAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = User.objects.filter(is_staff=True, is_superuser=False)
    serializer_class = RegisterSerializer


adminuser_list_view = AdminUserAPIView.as_view()


# Delete Admin User
class AdminUserkDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = User.objects.filter(is_staff=True, is_superuser=False)
    serializer_class = RegisterSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


adminuser_destory_view = AdminUserkDestroyAPIView.as_view()


# Find Admin User
class AdminUserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUser]
    queryset = User.objects.filter(is_staff=True, is_superuser=False)
    serializer_class = RegisterSerializer
    lookup_field = 'pk'


adminuser_detail_view = AdminUserDetailAPIView.as_view()


########################################### Dashboard ##########################################################
# Dashboard
@api_view(["GET"])
@permission_classes([IsAuthenticated,])
def dashboard(request):
    user = request.user
    if user.is_superuser:

        users = User.objects.filter(is_staff=False).count()
        adminusers = User.objects.filter(
            is_staff=True, is_superuser=False).count()
        categories = Category.objects.all().count()
        posts = Post.objects.all().count()
        primary_comment = Comment.objects.all().count()
        nested_comment = NestedComment.objects.all().count()
        comments = primary_comment + nested_comment
        return Response({"users": users, "adminusers": adminusers, "categories": categories, "posts": posts, "comments": comments})

    return Response({"Error": "UnAuthorized User"})


# Fetch Posts
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsSuperUserTwo])
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
        queryset = Post.objects.filter(title__icontains=search)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # Category Only
    if search == "" and category_id != "" and date == "":
        queryset = Post.objects.filter(category_id=category_id)
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
            posted_at__gte=date)
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
            posted_at__gte=date)
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
            category_id=category_id)
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
            posted_at__gte=date)
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
            posted_at__gte=date)
        if len(queryset) > 0:
            paginator = StandardResultsSetPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = PostSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({"detail": "Nothing Found"})

    # default
    queryset = Post.objects.all()
    if len(queryset) > 0:
        paginator = StandardResultsSetPagination()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        return Response({"detail": "Nothing Found"})


# fetch_comment
@api_view(["POST"])
@permission_classes([IsAuthenticated, IsSuperUserTwo])
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
