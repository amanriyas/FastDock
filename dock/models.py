from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User

# Create your models here.

class DockerfileRequest(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    stack_description = models.TextField()
    production_ready = models.BooleanField(default=False)
    generated_dockerfile = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.stack_description}"

    class Meta:
        db_table = "DockerfileRequest"


