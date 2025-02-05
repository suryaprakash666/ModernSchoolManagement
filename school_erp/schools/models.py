from django.db import models
from django.core.validators import EmailValidator, RegexValidator

class School(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(null=True, blank=True)
    principal = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(unique=True, validators=[EmailValidator()])
    contact_phone = models.CharField(
        max_length=15, 
        unique=True, 
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )

    class Meta:
        db_table = "school"
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.name
