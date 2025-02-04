from django.db import models
from django.core.validators import EmailValidator
import uuid

class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    principal = models.ForeignKey('staffs.Staff', on_delete=models.CASCADE, related_name='school_principal', null=True, blank=True)
    chairman = models.CharField(max_length=50)
    shareholder = models.CharField(max_length=50)
    establishment_date = models.DateField()
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True, validators=[EmailValidator])
    website = models.URLField()
    
    # Address
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()

    #controls
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    
    
    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'
        db_table = 'schools'
        
    def __str__(self):
        return self.name