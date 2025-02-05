from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class StaffRegister(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(validators=[EmailValidator()], null=True, blank=True)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        null=True,
        blank=True
    )
    documents_uploaded = models.JSONField(null=True, blank=True)  # List of document file paths or names
    registration_date = models.DateField(auto_now_add=True)
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, related_name='staff_registers')

    class Meta:
        db_table = "staff_register"
        verbose_name = "Staff Register"
        verbose_name_plural = "Staff Registers"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Staff(models.Model):
    user = models.ForeignKey('Baseuser.BaseUser', on_delete=models.CASCADE, related_name='staff')
    staff_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='staff_profiles/', null=True, blank=True)
    contact_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        null=True,
        blank=True
    )
    email = models.EmailField(validators=[EmailValidator()], null=True, blank=True)
    date_of_joining = models.DateField(auto_now_add=True)
    documents_verified = models.BooleanField(default=False)
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, related_name='staff_members')

    class Meta:
        db_table = "staff"
        verbose_name = "Staff"
        verbose_name_plural = "Staff Members"

    def __str__(self):
        return f"{self.staff_id} - {self.user.username}"
