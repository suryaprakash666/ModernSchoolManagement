import os
from django.conf import settings
from django.test import RequestFactory

os.environ['DJANGO_SETTINGS_MODULE'] = 'school_erp.settings'
import django
django.setup()

request = RequestFactory().get('/')
print(request.session.items())
