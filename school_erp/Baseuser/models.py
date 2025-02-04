import uuid
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.core.validators import EmailValidator

# Create your models here.
class BaseUser(AbstractUser, PermissionsMixin):
    # User Credentials
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=300)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)



    # User roles
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


    # User timestamps
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    id_validity = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'base_user'

    def __str__(self):
        return self.email
