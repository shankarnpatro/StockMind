import os
from calendar import timegm
from collections import namedtuple
from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from StockMind.settings import AUTH_USER_MODEL
from apps.restapi.serializers.users import UserCreateSerializer, UserLoginSerializer, UserSerializer, \
    UserUpdateSerializer, UserProfileImageSerializer, UserPasswordChangeSerializer, UserEmailVerificationSerializer
from apps.usermgmt.models import User
from apps.usermgmt.views import EmailVerification

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def jwt_payload_handler(user):
    payload = {
        'user_id': user.id,
        'username': user.phone,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )
    return payload


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserCreateSerializer(user, context={'request': request}).data
    }


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError:
            errors = []
            for key in serializer.errors:
                errors.append(serializer.errors[key][0].capitalize())
            return Response({"message": errors}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        return_data = serializer.data
        user = namedtuple("User", return_data.keys())(*return_data.values())
        if user.id > 0:
            # if CURRENT_DOMAIN == '127.0.0.1:8000':
            #     send_verification_email.delay(user)
            jwt_token = jwt_encode_handler(jwt_payload_handler(user))
            response = Response(return_data, status=status.HTTP_201_CREATED)
            response['X-AUTH-TOKEN'] = jwt_token
            return response
        else:
            return Response({'message': 'Unable to save user.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@receiver(post_save, sender=AUTH_USER_MODEL)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        email_verification = EmailVerification()
        email_verification.send_email(instance)


class EmailActivationView(generics.RetrieveAPIView, EmailVerification):
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        if self.activate(self.request, self.kwargs['pk'], self.kwargs['token']):
            return Response(template_name='email_verification_complete_template.html',
                            status=status.HTTP_200_OK)
        else:
            return Response(template_name='email_verification_failure_template.html',
                            status=status.HTTP_400_BAD_REQUEST)

    serializer_class = UserEmailVerificationSerializer


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def get(self, request, format=None):
        if request.user.is_authenticated:
            ser = UserSerializer(request.user, many=False)
            user = ser.instance
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            resp = Response(ser.data)
            resp['X-AUTH-TOKEN'] = token
            return resp
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            user = ser.instance
            request.user = user
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            userSer = UserSerializer(user, many=False)
            resp = Response(userSer.data)
            resp['X-AUTH-TOKEN'] = token
            return resp
        return Response(ser.errors, status=status.HTTP_401_UNAUTHORIZED)


@permission_classes((IsAuthenticated,))
class UpdateUserView(generics.RetrieveUpdateAPIView):
    """
    Accepted Fields : first_name, last_name
    """
    serializer_class = UserUpdateSerializer

    def get_queryset(self):
        return User.objects.all()

    def update(self, request, *args, **kwargs):
        mod_user = User.objects.get(id=self.kwargs['pk'])
        # user = self.request.user
        serializer = self.get_serializer(mod_user, data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        response_data = serializer.data
        return Response(response_data)


@permission_classes((IsAuthenticated,))
class UserProfileImageView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileImageSerializer

    def put(self, request, *args, **kwargs):
        user = request.user
        try:
            prof_image = User.objects.filter(id=user.id).values_list('profile_image', flat=True)[0]
            if prof_image != "":
                os.remove("media/" + prof_image)
                print("Delete Successful.")
        except IndexError:
            print("No Profile Image Found.")
        except FileNotFoundError:
            print("Delete Unsuccessful.")
        return super().put(request, *args, **kwargs)


@permission_classes((IsAuthenticated,))
class ChangePasswordView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPasswordChangeSerializer

    '''Needs Modification (reason : Swagger is failing to load because of this.)'''

    def get_serializer_context(self):
        return {"user_id": self.kwargs['pk']}

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
