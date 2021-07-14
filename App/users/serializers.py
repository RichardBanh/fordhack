from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Users


class UsersSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Users
        fields = (
            'uuid',
            'username',
            'phone_number',
            'email',
            'registration_date',
            'password',
            'is_staff',
            'is_admin',
            'is_superuser',
            'is_active'
        )
        extra_kwargs = {'password': {'write_only': True},}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



# 'is_staff': {'write_only': True},'is_admin': {'write_only': True},'is_superuser': {'write_only': True}}