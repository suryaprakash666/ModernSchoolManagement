# SchoolManagement/ManageSchool/tests.py

from django.test import TestCase, Client
from django.urls import reverse
import hashlib
from .ModelsOfDatabase.SchoolDataModel import Schooldatamodel

class SchoolLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('schoolloginlink')
        self.home_url = reverse('schoolhomeurl')

        self.email = 'test@example.com'
        self.passkey = 'testpasskey'
        self.hashed_passkey = hashlib.sha256(self.passkey.encode()).hexdigest()

        Schooldatamodel.objects.create(email=self.email, passkey=self.hashed_passkey, name='Test School',
                                       street='123 Test Street', city='Test City', locality='Test Locality',
                                       state='Test State')

    def test_school_login(self):
        response = self.client.post(self.login_url, {'email': self.email, 'passkey': self.passkey})

        # Print out the response status code and content
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.content}")

        # Check that the response is a redirect to the school home view
        self.assertRedirects(response, self.home_url)