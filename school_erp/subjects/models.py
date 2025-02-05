from django.db import models
from django.core.validators import MinLengthValidator

class Subject(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],  # Ensuring the name is at least 2 characters long
        null=False,
        blank=False
    )
    school = models.ForeignKey(
        'schools.School',
        on_delete=models.CASCADE,
        related_name='subjects',
        null=True,  # Allowing null values to avoid errors during migrations
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )

    teachers = models.ManyToManyField(
        'staffs.Staff',
        related_name='subjects',
        blank=True  # Allowing blank to avoid errors if no teachers are assigned
    )
    classes = models.ManyToManyField(
        'classes.Class',
        related_name='subjects_assigned',
        blank=True  # Allowing blank to avoid errors if no classes are assigned
    )
    sections = models.ManyToManyField(
        'classes.Section',
        related_name='subjects',
        blank=True  # Allowing blank to avoid errors if no sections are assigned
    )

    class Meta:
        db_table = "subject"
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name
