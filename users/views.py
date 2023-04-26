from rest_framework import generics, permissions, serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer, ActivationSerializer, ChangePasswordSerializer, PasswordTokenSerializer
from .models import ActivationModel, PasswordTokenModel
from accounts.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .permissions import IsUser


# SIGN UP


@api_view(['POST'])
@permission_classes([AllowAny,])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    _, token = AuthToken.objects.create(user)

    confirmation_token = default_token_generator.make_token(user)
    serializer2 = ActivationSerializer(data=request.data)
    serializer2.is_valid(raise_exception=False)
    addon = serializer2.save(user_id=user, token=confirmation_token)
    actiavation_link = f'http://localhost:8000/api/user/activation/{user.id}/{confirmation_token}/'
    # actiavation_link = f'http://localhost:8000/api/user/activation/?user_id={user.id}&confirmation_token={confirmation_token}'

    send_mail(
        subject='Activation Link',
        message=actiavation_link,
        from_email=settings.EMAIL_FROM_EMAIL,
        recipient_list=[user.email])

    return Response({
        'message': 'success',
        'token': token
    })

# ACTIVATION


@api_view(['GET'])
@permission_classes([AllowAny,])
def activation(request, **kwargs):
    user_id = kwargs['user_id']
    confirmation_token = kwargs['confirmation_token']

    try:
        user = User.objects.filter(id=user_id)
        if user.count() == 0:
            return Response({"Error": "User Not Found"}, status=404)
        userr = get_object_or_404(User, id=user_id)
        token = ActivationModel.objects.filter(
            user_id=user_id, token=confirmation_token)
        if token.count() == 0:
            return Response({"Error": "Invalid or Expired Token"}, status=404)

    except Exception as e:
        raise e

    userr.is_active = True
    userr.save()
    ActivationModel.objects.filter(
        user_id=user_id, token=confirmation_token).delete()

    return Response({"message": "User Account Verified Successfully"})

# LOGIN


@ api_view(['POST'])
@ permission_classes([AllowAny,])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

    if user.role == "USER":
        return Response({
            'token': token
        })
    return Response({"Error": "UnAuthorized User"})

# FETCH INFO


@ api_view(['GET'])
@ permission_classes([IsAuthenticated, IsUser])
def get_user_data(request):
    user = request.user
    return Response({
        'user_info': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'name': user.name
                    }
    })

# CHANGE PASSWORD


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.filter(is_staff=False)
    permission_classes = [IsAuthenticated, IsUser]
    serializer_class = ChangePasswordSerializer
    # lookup_field = 'pk'


change_passsword = ChangePasswordView.as_view()

# FORGET PASSWORD REQUEST


@ api_view(['POST'])
@ permission_classes([AllowAny,])
def forgetpassword_request(request):

    try:
        email_address = request.data['email']
        if email_address == "":
            # raise Exception("Email Field Not Found")
            return Response({"Error": "Email is required"}, status=404)

        checkUser = User.objects.filter(email=email_address)
        if checkUser.count() == 0:
            return Response({"Error": "User Not Found"}, status=404)
        userObj = get_object_or_404(User, email=request.data['email'])
        userData = RegisterSerializer(userObj).data

        TokenCheck = PasswordTokenModel.objects.filter(
            user_id=userData['id']).count()

        if TokenCheck > 0:
            TokenCheck = PasswordTokenModel.objects.filter(
                user_id=userData['id']).delete()

    except Exception as e:
        raise e

    confirmation_token = default_token_generator.make_token(userObj)
    serializer = PasswordTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=False)
    addon = serializer.save(
        user_id=userObj, token=confirmation_token)
    user_id = userData['id']
    actiavation_link = f'http://localhost:8000/api/user/password/reset/{user_id}/{confirmation_token}/'

    send_mail(
        subject='Password Reset',
        message=actiavation_link,
        from_email=settings.EMAIL_FROM_EMAIL,
        recipient_list=[userData['email']])

    return Response("Password Reset Mail has been sent")


# Password Reset
@ api_view(['POST'])
@ permission_classes([AllowAny,])
def password_rest(request, **kwargs):
    user_id = kwargs['user_id']
    confirmation_token = kwargs['confirmation_token']

    try:
        checkUser = User.objects.filter(id=user_id).count()
        if checkUser == 0:
            return Response({"Error": "User Not Found"}, status=404)
        user = get_object_or_404(User, id=user_id)
        token = PasswordTokenModel.objects.filter(
            user_id=user_id, token=confirmation_token).count()
        if token == 0:
            return Response({"Error": "Invalid or Expired Token"}, status=404)
        password = request.data['password']
        if password == "":
            return Response({"Error": "Password is required"}, status=404)
    except Exception as e:
        raise e

    PasswordTokenModel.objects.filter(user_id=user_id).delete()

    user.set_password(password)
    user.save()
    return Response("success")
