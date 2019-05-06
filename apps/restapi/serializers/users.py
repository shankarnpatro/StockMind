from django.contrib.auth import authenticate
from rest_framework import serializers

from apps.usermgmt.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'profile_image', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserCreateSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # print("Inside the Create Function")
        user = User.objects.create_complete_user(validated_data['first_name'],
                                                 validated_data['last_name'],
                                                 validated_data['phone'],
                                                 validated_data['email'],
                                                 validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=10, required=True)
    password = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ['phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs, ):
        user = authenticate(
            phone=attrs['phone'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError('invalid credentials provided')
        self.instance = user
        return user


class UserUpdateSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        try:
            instance.first_name = validated_data.get('first_name')
            instance.last_name = validated_data.get('last_name')
            instance.save()
            return instance
        except Exception as e:
            print(str(e))

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('password', 'last_login', 'is_superuser', 'phone', 'profile_image',
                            'email', 'is_active', 'is_staff', 'is_admin', 'groups', 'user_permissions')


class UserProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('profile_image',)


class UserPasswordChangeSerializer(serializers.ModelSerializer):  # password change serializers class
    old_password = serializers.CharField(write_only=True)
    password = serializers.CharField(required=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'confirm_password')

    def validate(self, validated_data):
        user_id = self.context["user_id"]
        user = User.objects.get(pk=user_id)
        if user.check_password(validated_data['old_password']):
            if validated_data['confirm_password'] != validated_data['password']:
                raise serializers.ValidationError({'password': 'Password must be confirmed correctly.'})
            return validated_data
        raise serializers.ValidationError({'old_password': 'Incorrect old password'})

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class UserEmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
