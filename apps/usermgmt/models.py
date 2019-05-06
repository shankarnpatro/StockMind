from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin,
)
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        # user.set_unusable_password(password)
        user.save(using=self._db)
        return user

    def create_complete_user(self, first_name, last_name, phone, email, password=None):
        if not phone:
            raise ValueError('Users must have a phone')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=UserManager.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            email,
            password=password,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


FIRST_NAME_LAST_NAME_REGEX = '^[a-zA-Z. ]*$'
PHONE_NUMBER_REGEX = '^[0-9]*$'


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True, validators=[RegexValidator(
        regex=FIRST_NAME_LAST_NAME_REGEX,
        message='first_name must be Alphanumeric or contain any of the following: a-zA-Z. ',
        code='invalid_name'
    )])
    last_name = models.CharField(max_length=100, blank=True, validators=[RegexValidator(
        regex=FIRST_NAME_LAST_NAME_REGEX,
        message='last_name must be Alphanumeric or contain any of the following: a-zA-Z. ',
        code='invalid_name'
    )])
    phone = models.CharField(max_length=10, blank=False, unique=True, validators=[RegexValidator(
        regex=PHONE_NUMBER_REGEX,
        message='name must be Alphanumeric or contain any of the following: ". @ + -" ',
        code='invalid_name'
    )])
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    profile_image = models.ImageField(upload_to='images/profile', blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        if full_name.strip() == "":
            return self.email
        else:
            return full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
