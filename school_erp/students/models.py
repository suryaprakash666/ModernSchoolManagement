from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator, RegexValidator

class StudentRegister(models.Model):
    first_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        validators=[MinLengthValidator(2)]
    )
    last_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        validators=[MinLengthValidator(2)]
    )
    email = models.EmailField(
        null=True, 
        blank=True, 
        validators=[EmailValidator()]
    )
    phone_number = models.CharField(
        max_length=15, 
        null=True, 
        blank=True, 
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$', 
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    documents_uploaded = models.JSONField(null=True, blank=True)  # Storing file paths or names of uploaded docs
    admission_request_date = models.DateField(auto_now_add=True)
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, related_name='student_registers')
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending'
    )

    class Meta:
        db_table = "student_register"
        verbose_name = "Student Register"
        verbose_name_plural = "Student Registers"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Student(models.Model):
    user = models.ForeignKey('Baseuser.BaseUser', on_delete=models.CASCADE, related_name='students')
    roll_number = models.CharField(
        max_length=20, 
        unique=True, 
        validators=[MinLengthValidator(1), MaxLengthValidator(20)]
    )
    class_level = models.ForeignKey('classes.Class', on_delete=models.CASCADE, related_name='students')
    section = models.ForeignKey('classes.Section', on_delete=models.CASCADE, related_name='students')
    admission_date = models.DateField(null=True, blank=True)
    parent_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        validators=[MinLengthValidator(2)]
    )
    parent_contact = models.CharField(
        max_length=15, 
        null=True, 
        blank=True, 
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$', 
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    parent_email = models.EmailField(
        null=True, 
        blank=True, 
        validators=[EmailValidator()]
    )
    profile_picture = models.ImageField(upload_to='student_profiles/', null=True, blank=True)
    documents_verified = models.BooleanField(default=False)  # To indicate if documents are verified

    class Meta:
        db_table = "student"
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.roll_number} - {self.user.username}"
