from django.db import models
from django.utils import timezone

    
class Schooldatamodel(models.Model):
    School_Id = models.AutoField(primary_key=True)
    School_Name = models.CharField(max_length=100)
    School_Email = models.EmailField(max_length=100)
    School_Key = models.CharField(max_length=100)
    School_Established = models.DateField(default=timezone.now)
    School_State = models.CharField(max_length=50)
    School_District = models.CharField(max_length=50)
    School_Locality = models.CharField(max_length=50)
    School_Pincode = models.CharField(max_length=50)

    def __str__(self):
        return self.School_Name

    class Meta:
        db_table = 'SchoolData'


class Staffdatamodel(models.Model):
    Staff_ID = models.CharField(max_length=10, primary_key=True)
    Staff_Password = models.CharField(unique=True, max_length=15, null=True)
    Staff_Firstname = models.CharField(max_length=100)
    Staff_Lastname = models.CharField(max_length=100)
    Staff_Profilepic = models.ImageField(upload_to='UserUploadedFiles/', default='')
    Staff_Adharpic = models.ImageField(upload_to='UserUploadedFiles/', default='')
    Staff_Qualification = models.CharField(max_length=50, choices=(
        ('Post Graduation','Post Graduate'),
        ('Graduation','Graduate'),
        ('Higher Secondary School', 'HS School')
    ))
    Staff_JoiningDate = models.DateField(default=timezone.now)
    Staff_Salary = models.CharField(max_length=10)
    Staff_Position = models.CharField(max_length=20, choices=(
        ('Teacher_Level A+', 'TA+'),
        ('Teacher_Level A', 'TA'),
        ('Teacher_Level B', 'B'),
        ('Teacher_Level C', 'C'),
        ('Support Staff', 'SST')
    ))
    School_Name = models.ForeignKey(Schooldatamodel, on_delete=models.CASCADE, related_name='staff')
    Staff_State = models.CharField(max_length=50)
    Staff_District = models.CharField(max_length=50)
    Staff_Locality = models.CharField(max_length=50)
    Staff_Pincode = models.CharField(max_length=50)

    def __str__(self):
        return self.Staff_ID

    class Meta:
        db_table = 'StaffData'


class Studentdatamodel(models.Model):
    Student_Id = models.AutoField(primary_key=True)
    Student_Password = models.CharField(unique=True, max_length=15, null=True)
    Student_Firstname = models.CharField(max_length=20)
    Student_Lastname = models.CharField(max_length=20)
    Student_DateofBirth = models.DateField(default=timezone.now)
    Student_Passportphoto = models.ImageField(upload_to='UserUploadedFiles/', default='')
    Student_Adharphoto = models.ImageField(upload_to='UserUploadedFiles/', default='')
    Student_CurrentStandard = models.CharField(max_length=10)
    Student_PreviousStandard = models.CharField(max_length=10)
    Student_Qualification = models.CharField(max_length=50, choices=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    ))
    Student_Contact = models.CharField(max_length=20)
    Student_Joindate = models.DateField(default=timezone.now)
    StudentID_Validation = models.DateField(default=timezone.now)
    Student_State = models.CharField(max_length=50)
    Student_District = models.CharField(max_length=50)
    Student_Locality = models.CharField(max_length=50)
    Student_Pincode = models.CharField(max_length=50)    
    Student_School = models.ForeignKey(Schooldatamodel, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.Student_Firstname + ' ' + self.Student_Lastname

    class Meta:
        db_table = 'StudentData'
