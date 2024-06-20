import os
import django
from SchoolManagement.ManageSchool.ModelsOfDatabase.SchoolDataModel import Schooldatamodel

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SchoolManagement.settings')
django.setup()


def check_school_exists(email, passkey):
    return Schooldatamodel.objects.filter(email=email, passkey=passkey).exists()

# Replace 'test_email' and 'test_passkey' with the actual email and passkey you want to check
email = 'maha@gmail.com'
passkey = 'maha123'

if check_school_exists(email, passkey):
    print(f"A school with email {email} and passkey {passkey} exists in the database.")
else:
    print(f"No school with email {email} and passkey {passkey} exists in the database.")