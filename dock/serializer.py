from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class DockerfileRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DockerfileRequest
        fields = '__all__'



