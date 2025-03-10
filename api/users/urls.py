from django.urls import path
from .views.loginview import SignupView, LoginView,create_superuser
from .views.instructor import InstructorView
from .views.student import StudentView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('instructor/<int:instructor_id>/', InstructorView.as_view()),
    path('student/<int:student_id>/', StudentView.as_view()),
    path('create/user/', create_superuser),
]