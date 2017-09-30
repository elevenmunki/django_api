# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#import TestCase from django.test
from django.test import TestCase
from .models import Bucketlist

#single test to test whether the model can create a bucketlist with a name
class Mode1TestCase(TestCase):
    """This class defines the test suite for the bucketlist"""

    def setUp(self):
        """Define the test client and other test variables."""
        self.cleint = APIClient()
        self.bucketlist_data = {'name': 'Go to Iceland!'}
        self.bucketlist = Bucketlist(name=self.bucketlist_name)
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
