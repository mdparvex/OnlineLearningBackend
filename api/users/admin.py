from django.contrib import admin
from .models.authentication import Authentication
from .models.Instructors import Instructor
from .models.students import Student

# Register your models here.
admin.site.register(Authentication)
admin.site.register(Instructor)
admin.site.register(Student)