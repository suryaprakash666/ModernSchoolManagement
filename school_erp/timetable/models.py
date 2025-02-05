from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Timetable(models.Model):
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE, related_name='timetables', null=True, blank=True)
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE, related_name='timetables', null=True, blank=True)
    class_level = models.ForeignKey('classes.Class', on_delete=models.CASCADE, related_name='timetables', null=True, blank=True)
    teacher = models.ForeignKey('staffs.Staff', on_delete=models.CASCADE, related_name='timetables', null=True, blank=True)
    day_of_week = models.CharField(
        max_length=9, 
        choices=[
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
            ('Saturday', 'Saturday'),
            ('Sunday', 'Sunday'),
        ],
        null=True, 
        blank=True
    )
    start_time = models.TimeField(null=True, blank=True)  # Starting time of the class
    end_time = models.TimeField(null=True, blank=True)  # Ending time of the class
    period = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],  # Assuming periods range from 1 to 10
        null=True, 
        blank=True
    )
    
    # To track if the class was taken or not
    class_taken = models.BooleanField(default=False)  # Whether the class was conducted
    teacher_present = models.BooleanField(default=False)  # Whether the teacher was present

    class Meta:
        db_table = "timetable"
        verbose_name = _("Timetable")
        verbose_name_plural = _("Timetables")

    def __str__(self):
        return f"{self.subject.name if self.subject else 'No Subject'} ({self.teacher.username if self.teacher else 'No Teacher'}) - {self.day_of_week} {self.start_time} - {self.end_time}"
