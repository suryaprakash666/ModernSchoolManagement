from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Class(models.Model):
    GRADE_CHOICES = [
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
        ('11', 'Grade 11'),
        ('12', 'Grade 12'),
    ]

    name = models.CharField(max_length=100, null=True, blank=True)  # Name of the class (e.g., "10th Grade")
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, related_name='classes', null=True, blank=True)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2100)], null=True, blank=True)  # Year the class belongs to (e.g., 2025)
    total_students = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # Total number of students in the class
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, null=True, blank=True)  # Grade of the class (1 to 12)
    subjects = models.ManyToManyField('subjects.Subject', related_name='class_levels', blank=True)  # Subjects taught in the class

    class Meta:
        db_table = "class"
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return f"{self.name} ({self.year})"


class Section(models.Model):
    class_level = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='sections', null=True, blank=True)  # Reference to Class model
    name = models.CharField(max_length=10, null=True, blank=True)  # Section name (e.g., "A", "B", etc.)
    total_students = models.IntegerField(default=0, validators=[MinValueValidator(0)])  # Total number of students in the section

    class Meta:
        db_table = "section"
        verbose_name = "Section"
        verbose_name_plural = "Sections"

    def __str__(self):
        return f"{self.class_level.name} - Section {self.name}"
