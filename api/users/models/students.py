from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings

class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=100)
    photo = models.FileField(upload_to='learning/images', null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        if self.first_name is None or self.first_name== "":
            return str(self.student_id)
        else:
            return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['-student_id']


class StudentSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, obj):
        if obj.photo:
            return settings.MEDIA_URL + str(obj.photo)  # Ensures correct URL format
        return None
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "photo"]

class StudentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "photo"]