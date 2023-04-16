from rest_framework import serializers, validators
from accounts.models import User
from .models import ActivationModel, PasswordTokenModel


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'email',
            'name'
        )

        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "Email has been taken"
                    )
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        email = validated_data.get("email")
        name = validated_data.get("name")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            name=name
        )

        return user


class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivationModel
        fields = [
            'user_id',
            'token'
        ]


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class PasswordTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordTokenModel
        fields = [
            'user_id',
            'token'
        ]
