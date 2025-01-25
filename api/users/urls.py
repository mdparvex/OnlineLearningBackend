from django.urls import path
from .views.loginview import SignupView, LoginView
from .views.user import UserView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/<int:user_id>/', UserView.as_view()),
]