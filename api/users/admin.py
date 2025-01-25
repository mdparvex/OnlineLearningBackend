from django.contrib import admin
from .models.authentication import Authentication
from .models.user import User

# Register your models here.
admin.site.register(Authentication)
admin.site.register(User)