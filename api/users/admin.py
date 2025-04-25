from django.contrib import admin
from .models.authentication import Authentication
from .models.Instructors import Instructor
from .models.students import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'created_at', 'updated_at')
    search_fields = ('first_name',)
    list_filter = ('created_at',)

# Register your models here.
admin.site.register(Authentication)
admin.site.register(Instructor)
admin.site.register(Student, StudentAdmin)