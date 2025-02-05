from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxLengthValidator

class BaseUser(AbstractUser):
    USER_TYPES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
    ]
    user_type = models.CharField(
        max_length=10, 
        choices=USER_TYPES, 
        null=True, 
        blank=True, 
        validators=[MaxLengthValidator(10)]
    )
    school = models.ForeignKey(
        'schools.School', 
        on_delete=models.CASCADE, 
        related_name="users", 
        null=True, 
        blank=True
    )

    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='baseuser_groups', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='baseuser_permissions', 
        blank=True
    )

    class Meta:
        db_table = "baseuser"

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
