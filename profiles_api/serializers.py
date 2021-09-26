from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our API view"""
    """Serializers ensures a certain data is of type when being passed onto an API"""
    name = serializers.CharField(max_length=10)
    Last_Name = serializers.CharField(max_length=10)