from rest_framework import serializers, validators
from accounts.models import User


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
        role = "ADMIN"

        user = User.objects.create_staff(
            username=username,
            password=password,
            email=email,
            name=name,
            role=role
        )

        return user
