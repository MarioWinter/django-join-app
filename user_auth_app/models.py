from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser model.
    Methods
    -------
    create_user(email, password=None, **extra_fields)
        Creates and returns a user with the given email and password.
    create_superuser(email, password=None, **extra_fields)
        Creates and returns a superuser with the given email and password.
    """
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    CustomUser model that extends AbstractBaseUser and PermissionsMixin.
    Attributes:
        email (EmailField): The email address of the user, used as the unique identifier.
        username (CharField): The username of the user, optional.
        first_name (CharField): The first name of the user, optional.
        last_name (CharField): The last name of the user, optional.
        phone (CharField): The phone number of the user, optional, validated by a regex.
        bgcolor (CharField): The background color preference of the user, optional.
        is_active (BooleanField): Indicates whether the user is active.
        is_staff (BooleanField): Indicates whether the user has staff privileges.
        date_joined (DateTimeField): The date and time when the user joined.
    Methods:
        __str__(): Returns the email of the user.
        get_full_name(): Returns the full name of the user.
        get_short_name(): Returns the short name of the user, which is the username if available, otherwise the part of the email before the '@'.
    """
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?\d{1,3}?\d{4,14}$', message="Enter a valid phone number."),],
        blank=True,
        null=True
    )
    bgcolor = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.username or self.email.split('@')[0]


    
    