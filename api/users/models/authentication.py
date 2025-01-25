from django.db import models
from rest_framework import serializers
from django.core.validators import MinLengthValidator


# authentication Model
class Authentication(models.Model):
    USER_TYPES = (
        ('1', 'Instructor'),
        ('2', 'Student'),
    )

    auth_id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, unique=True)
    password = models.CharField(max_length=100, validators=[MinLengthValidator(6)], null=True, blank=True)
    auth_token = models.CharField(max_length=100, null=True, blank=True)
    user_type = models.CharField(max_length=100, choices=USER_TYPES)
    user_id = models.BigIntegerField()
    temp_password = models.CharField(max_length=200, null=True, blank=True)
    temp_password_valid_time = models.DateTimeField(null=True, blank=True)
    total_login_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-auth_id']


class AuthenticationSerializer(serializers.ModelSerializer):

    def validate_email(self, value):
        lower_email = value.lower()
        if Authentication.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Email already exists")
        return lower_email

    def validate_username(self, value):
        lower_username = value.lower()
        if Authentication.objects.filter(username__iexact=lower_username).exists():
            raise serializers.ValidationError("Username already exists")
        return lower_username

    class Meta:
        model = Authentication
        fields = '__all__'
