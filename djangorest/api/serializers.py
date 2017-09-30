#api/serializers.py

#serialize and deserialize data (changing data from complex quersets from the
#db to form JSON or XML)
#deserializing is reverting this process after validating the data we want to save in db

#ModelSerializer class lets you automaticall create a Serializer class with fields
#that correspond to the Model fields

from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

class Meta:
    """Meta class to map serializer's fields with the model fields."""
    model = Bucketlist
    fields = ('id', 'name', 'date_created', 'date_modified')
    read_only_fields = ('date_created', 'date_modified')
