from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models.students import Student, StudentSerializer,StudentUpdateSerializer

class StudentView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request, student_id):
        content = {
            "status": 0
        }

        try:
            user = Student.objects.get(student_id=student_id)
        except:
            content['massage']='User not found'
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)
        user_data = StudentSerializer(user).data
        content['status']=1
        content['user_data'] = user_data
        return JsonResponse(content, status=status.HTTP_200_OK)

    def post(self,request, user_id):
        pass

    def patch(self, request, student_id):
        content={}
        try:
            user_instance = Student.objects.get(student_id=student_id)
        except:
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)
        data = StudentUpdateSerializer(instance=user_instance, data=request.data)

        if data.is_valid():
            data.save()
            content['massage'] = 'updated successfully'
            return JsonResponse(content, status=status.HTTP_200_OK)
        else:
            content['massage'] = 'failed'
            return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, student_id):
        content={}
        try:
            user_instance = Student.objects.get(student_id=student_id)
        except:
            content['massage']='User not found'
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)
        user_instance.delete()
        content['massage']='Deleted successfully'
        return JsonResponse(content, status=status.HTTP_200_OK)