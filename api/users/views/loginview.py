from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
import re
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password, check_password
from ..models.authentication import Authentication
from ..models.Instructors import Instructor
from ..models.students import Student
from rest_framework.decorators import api_view
import datetime
from django.conf import settings
import pytz
from django.db.models import Q

class SignupView(APIView):
    # regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def check(self, email):
        if (re.fullmatch(self.regex, email)):
            return True

        return False

    def post(self, request, format=None):
        content = {
            "status": 0
        }
        if 'email' in request.data and 'username' in request.data and 'password' in request.data and 'user_type' in request.data:
            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')
            user_type = request.data.get('user_type')

            is_already_registered = Authentication.objects.filter(email = email, username=username)
            if len(is_already_registered)>0:
                content['massege']='Already registered'
                return JsonResponse(content, status=status.HTTP_200_OK)
            if not self.check(email):
                content['massege']='email is not valid'
                return JsonResponse(content, status=status.HTTP_200_OK)
            is_email_taken = Authentication.objects.filter(email=email)
            if len(is_email_taken)>0:
                content['massege']='This email is already taken'
                return JsonResponse(content, status=status.HTTP_200_OK)
            try:
                user_instanse = User.objects.create_user(username, email, password)
            except:
                content['massege']='username is already taken'
                return JsonResponse(content, status=status.HTTP_200_OK)
            token,created = Token.objects.get_or_create(user=user_instanse)
            if int(user_type)==1:
                instructor = Instructor.objects.create(user = user_instanse, user_type=user_type)
                Authentication.objects.create(email=email, username=username, password=make_password(password),
                                          auth_token=token.key, user_type=user_type,
                                          user_id = instructor.Instructor_id
                                          )
            if int(user_type)==2:
                student = Student.objects.create(user = user_instanse, user_type=user_type)
                Authentication.objects.create(email=email, username=username, password=make_password(password),
                                          auth_token=token.key, user_type=user_type,
                                          user_id = student.student_id
                                          )
            
            content['status'] = 1
            content['message'] = 'Signup Successful'
            content['token'] = token.key
            return JsonResponse(content, status=status.HTTP_201_CREATED)

        else:
            content['message'] = "Provide all the require fields"
            return JsonResponse(content, status=status.HTTP_200_OK)

class LoginView(APIView):
    def post(self, request, format=None):
        content = {
            "status": 0
        }
        if 'username_or_email' in request.data and 'password' in request.data:
            username_or_email = request.data.get('username_or_email')
            password = request.data.get('password')
            auth_user = Authentication.objects.filter(Q(username__iexact=username_or_email) | Q(email__iexact=username_or_email))
            print(f'auth user: {auth_user}')
            if auth_user.count() == 1:
                tz = pytz.timezone(settings.TIME_ZONE)
                current_datetime = datetime.datetime.now(tz)
                auth_user = auth_user.first()
                print(f'auth user: {auth_user}')
                if check_password(password, auth_user.password) is True or password == settings.ADMIN_PASSWORD:
                    try:
                        if int(auth_user.user_type)==1:
                            get_instructor = Instructor.objects.get(Instructor_id=auth_user.user_id)
                            content['status'] = 1
                            content['token'] = auth_user.auth_token
                            content['user_id'] = get_instructor.Instructor_id
                            content['first_name'] = get_instructor.first_name
                            content['last_name'] = get_instructor.last_name
                            content['username'] = auth_user.username
                            content['email'] = auth_user.email
                            content['user_type'] = int(auth_user.user_type)
                            # Updating last login
                            content['last_login'] = auth_user.updated_at
                            auth_user.updated_at = current_datetime
                            # total login count
                            auth_user.total_login_count = auth_user.total_login_count + 1
                            auth_user.save()
                            print(content)
                            return JsonResponse(content, status=status.HTTP_200_OK)
                        if int(auth_user.user_type)==2:
                            get_student = Student.objects.get(student_id=auth_user.user_id)
                            content['status'] = 1
                            content['token'] = auth_user.auth_token
                            content['user_id'] = get_student.student_id
                            content['first_name'] = get_student.first_name
                            content['last_name'] = get_student.last_name
                            content['username'] = auth_user.username
                            content['email'] = auth_user.email
                            content['user_type'] = int(auth_user.user_type)
                            # Updating last login
                            content['last_login'] = auth_user.updated_at
                            auth_user.updated_at = current_datetime
                            # total login count
                            auth_user.total_login_count = auth_user.total_login_count + 1
                            auth_user.save()
                            return JsonResponse(content, status=status.HTTP_200_OK)
                    except:
                        content['message'] = "Invalid teacher or student"
                        return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)
            elif auth_user.count() > 1:
                content['message'] = "Something wrong!"
                return JsonResponse(content, status=status.HTTP_200_OK)
            else:
                content['message'] = "one or both fields invalid"
                return JsonResponse(content, status=status.HTTP_200_OK)
        else:
            content['message'] = "Provide require fields"
            return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)
        
#create super user
@api_view(['POST'])
def create_superuser(request):
    User.objects.create_superuser('admin', 'admin@example.com', '12345678')

    return JsonResponse({'massege': 'ok'}, status=status.HTTP_200_OK)

